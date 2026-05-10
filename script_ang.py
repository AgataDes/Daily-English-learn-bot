import os
import requests
import random
from deep_translator import GoogleTranslator


DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK')

def fetch_data():
    url = "https://raw.githubusercontent.com/jnoodle/English-Vocabulary-Word-List/refs/heads/master/Oxford%205000.txt"
    response = requests.get(url)

# .splitlines() tnie tekst tam, gdzie jest nowa linia
    lines = response.text.splitlines()
    chosen_line = random.choice(lines)
    word = chosen_line.split()[0]
    translation = GoogleTranslator(source='en', target='pl').translate(word)
    message = f"Oto Twoje słowo na dziś: **{word}**\nPo polsku: **{translation}**"
    return message



def send_to_discord(message):
    payload ={"content": message}
    requests.post(DISCORD_WEBHOOK_URL, json=payload)


if __name__ == "__main__":
    content = fetch_data()
    send_to_discord(content)

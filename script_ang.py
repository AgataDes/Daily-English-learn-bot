import os
import requests
import random
from deep_translator import GoogleTranslator


deepl_link = f"https://www.deepl.com/write"
reverso_link = f"https://context.reverso.net/translation/english-polish/{word}"




DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK')

def fetch_data():
    url = "https://raw.githubusercontent.com/jnoodle/English-Vocabulary-Word-List/refs/heads/master/Oxford%205000.txt"
    response = requests.get(url)

# .splitlines() tnie tekst tam, gdzie jest nowa linia
    lines = response.text.splitlines()
    chosen_line = random.choice(lines)
    word = chosen_line.split()[0]
    translation = GoogleTranslator(source='en', target='pl').translate(word)
    message = (
        f"### 🇬🇧 Word of the Day: **{word.upper()}**\n"
        f"🇵🇱 **Tłumaczenie:** {translation}\n"
        f"--- \n"
        f"💪 **Twoje zadanie:** Ułóż zdanie z tym słowem i sprawdź je tutaj:\n"
        f"👉 [DeepL Write - Popraw błędy]({deepl_link})\n"
        f"👉 [Reverso Context - Przykłady użycia]({reverso_link})"
    )
    return message



def send_to_discord(message):
    payload ={"content": message}
    requests.post(DISCORD_WEBHOOK_URL, json=payload)


if __name__ == "__main__":
    content = fetch_data()
    send_to_discord(content)

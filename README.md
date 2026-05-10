# 🇬🇧 Daily English Word Bot

A simple yet effective Python-based bot that automates English language learning. Every day, the bot randomly selects a word from the **Oxford 5000** list, translates it into Polish, and sends a complete study kit to a Discord channel.

##  Motivation
The primary goal of this project, besides technical practice, is to foster a **healthy daily routine**by automating the delivery of a new word each morning.
##  How it works
1. **GitHub Actions**: Triggers a virtual environment every day at 10:00 AM (CET).
2. **Python Script**: Downloads the latest word list, picks a random entry, and translates it using the `deep-translator` library.
3. **Discord Integration**: The result is sent via Webhook as a formatted message.

## 🛠️ Technologies
*   **Language:** Python 3.x
*   **Automation:** GitHub Actions
*   **Libraries:** `requests`, `deep_translator`
*   **Data Source:** Oxford 5000 Word List

##  Message Features
Each message sent by the bot includes:
*   ✅ **Word of the Day** (Bolded and Uppercase).
*   ✅ **Polish Translation**.
*   ✅ **DeepL Write Link** to check the grammar of your own practice sentences.
*   ✅ **Reverso Context Link** to see real-world examples of the word in use.

## ⚙️ Setup & Configuration
To run your own instance:
1. Clone the repository.
2. Create a Webhook on your Discord server.
3. Add the Webhook URL to your **GitHub Secrets** under the name `DISCORD_WEBHOOK`.
4. The bot will run automatically based on the schedule defined in `.github/workflows/main.yml`.

---
*Project created for learning automation and building consistent personal growth habits.*
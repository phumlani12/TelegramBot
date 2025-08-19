# Mood Support Telegram Bot

## Problem Addressed
This bot provides motivational or supportive messages based on how the user is feeling. It helps users cope with stress or celebrate positive moods.

## How to Run
1. Clone the repository:
   git clone <your-repo-url>
2. Create and activate a virtual environment:
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate      # Windows
3. Install dependencies:
   pip install -r requirements.txt
4. Add your Telegram Bot Token in main.py
5. Run the bot:
   python main.py
6. Open Telegram, search your bot by username, press Start, and send a message describing your mood.

## Limitations
- Only detects basic keywords related to emotions.
- Complex or nuanced messages may receive a generic response.
- The bot cannot provide professional mental health advice.

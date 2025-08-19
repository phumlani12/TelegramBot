#!/usr/bin/python3
import spacy
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import random


nlp = spacy.load("en_core_web_sm")


support_messages = [
    "Keep going, you’re doing great!",
    "Remember to take deep breaths and relax.",
    "Every day is a new opportunity!",
    "You’ve got this, don’t give up!",
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your Mood Support Bot. How are you feeling today?")

async def respond(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    doc = nlp(user_text)



    if any(word.text.lower() in ["sad", "upset", "unhappy", "frustrated"] for word in doc):
        reply = random.choice(support_messages)
    elif any(word.text.lower() in ["happy", "great", "good", "excited"] for word in doc):
        reply = "I’m glad to hear that! Keep smiling 😊"
    else:
        reply = "Thanks for sharing! Stay positive and take care."

    await update.message.reply_text(reply)

if __name__ == "__main__":
    app = ApplicationBuilder().token("8497620771:AAEg2l_yzGFMVgQB88OKbC-nnbBUBcRjWJQ").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond))
    app.run_polling()

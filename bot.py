import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Bot commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = "Welcome to VnHax Official! Please choose an option below to get started:"
    keyboard = [
        [InlineKeyboardButton("🗣️ Inquiry / سؤال", url="https://t.me/+2O18lpzpF_ZiZjY1")],
        [InlineKeyboardButton("📢 Official Channel / القناة الرسمية", url="https://t.me/+2O18lpzpF_ZiZjY1")],
        [InlineKeyboardButton("🛒 Purchase Now / شراء الآن", url="https://t.me/Thesqd")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

def main():
    # Bot Token
    TOKEN = os.getenv("BOT_TOKEN", "7327073775:AAHS77p3lmuj9iMUMTbBcZ7iq6xakBzRK6o")

    # Initialize the Application
    application = Application.builder().token(TOKEN).build()

    # Command Handlers
    application.add_handler(CommandHandler("start", start))

    # Start the Bot
    application.run_polling()

if __name__ == "__main__":
    main()

from telegram import Update
from telegram.ext import Application, CommandHandler
import logging

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Use Application instead of Updater
async def start(update: Update, context):
    # Define the reply message with buttons
    welcome_message = """
    Welcome to VnHax Official Bot! Choose an option below:
    """
    
    # You can add buttons here (e.g., inline buttons or keyboard buttons)
    # Example:
    reply_markup = {
        "inline_keyboard": [
            [
                {"text": "🗣️ Inquiry / سؤال", "url": "https://t.me/+2O18lpzpF_ZiZjY1"},
                {"text": "📢 Official Channel / القناة الرسمية", "url": "https://t.me/+2O18lpzpF_ZiZjY1"},
                {"text": "🛒 Purchase Now / شراء الآن", "url": "https://t.me/Thesqd"}
            ]
        ]
    }

    # Send welcome message with buttons
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

def main():
    # Create Application instance using the bot token
    application = Application.builder().token("7327073775:AAHS77p3lmuj9iMUMTbBcZ7iq6xakBzRK6o").build()

    # Add the handler for the /start command
    application.add_handler(CommandHandler("start", start))

    # Run the bot
    application.run_polling()

if __name__ == '__main__':
    main()

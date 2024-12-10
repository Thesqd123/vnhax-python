from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from tenacity import retry, stop_after_attempt, wait_fixed, RetryError
import logging

# Your Bot Token
TOKEN = "7327073775:AAHS77p3lmuj9iMUMTbBcZ7iq6xakBzRK6o"

# Request kwargs to set a custom timeout
request_kwargs = {
    'timeout': 120  # Increased timeout to 120 seconds
}

# Initialize Updater with token and custom request kwargs
updater = Updater(TOKEN, request_kwargs=request_kwargs, use_context=True)

# Retry the main bot loop in case of failure
@retry(stop=stop_after_attempt(5), wait=wait_fixed(10))
def main():
    try:
        # Add handlers for your bot's commands
        def start(update: Update, context: CallbackContext):
            update.message.reply_text("Welcome to the bot!")

        # Add command handler for '/start'
        updater.dispatcher.add_handler(CommandHandler("start", start))

        # Start polling for updates
        print("Bot started. Waiting for updates...")
        updater.start_polling()
    
    except RetryError as e:
        logging.error(f"Bot failed after retries: {e}")
        raise  # If retry fails after 5 attempts, raise the error

if __name__ == "__main__":
    # Setting up logging
    logging.basicConfig(level=logging.INFO)
    
    main()

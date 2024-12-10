from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update

# Your bot token
TOKEN = "7327073775:AAHS77p3lmuj9iMUMTbBcZ7iq6xakBzRK6o"

# Custom timeout configuration (adjust as needed)
request_kwargs = {
    'read_timeout': 20,  # 20 seconds to read data from Telegram
    'connect_timeout': 20  # 20 seconds to establish connection to Telegram
}

# Function to start the bot
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Welcome to the VnHax Official Bot!\n\n"
        "Please choose one of the options below:\n"
        "🗣️ Inquiry / سؤال - https://t.me/+2O18lpzpF_ZiZjY1\n"
        "📢 Official Channel / القناة الرسمية  - https://t.me/+2O18lpzpF_ZiZjY1\n"
        "🛒 Purchase Now / شراء الآن  - https://t.me/Thesqd"
    )

# Initialize Updater with the token and custom timeouts
updater = Updater(token=TOKEN, request_kwargs=request_kwargs, use_context=True)

# Dispatcher to handle commands
dispatcher = updater.dispatcher

# Add command handler for '/start'
dispatcher.add_handler(CommandHandler('start', start))

# Start polling for updates (to keep bot running)
updater.start_polling()

# Idle to keep the bot running
updater.idle()

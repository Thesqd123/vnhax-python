import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from tenacity import retry, stop_after_attempt, wait_fixed

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Your Bot Token
TOKEN = "7327073775:AAHS77p3lmuj9iMUMTbBcZ7iq6xakBzR"

# Retry decorator to handle connection issues
@retry(stop=stop_after_attempt(5), wait=wait_fixed(2))
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Respond to the /start command with welcome message and links."""
    welcome_message = (
        "Welcome to the bot! How can I assist you?\n\n"
        "🗣️ **Inquiry / سؤال** - [Click Here](https://t.me/+2O18lpzpF_ZiZjY1)\n"
        "📢 **Official Channel / القناة الرسمية** - [Click Here](https://t.me/+2O18lpzpF_ZiZjY1)\n"
        "🛒 **Purchase Now / شراء الآن** - [Click Here](https://t.me/Thesqd)"
    )
    await update.message.reply_text(welcome_message, parse_mode="Markdown")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Respond to the /help command."""
    await update.message.reply_text("Available commands: /start, /help")

async def main() -> None:
    """Run the bot."""
    application = Application.builder().token(TOKEN).build()

    # Command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Start polling for updates
    logger.info("Starting the bot...")
    await application.run_polling()

if __name__ == "__main__":
    import asyncio

    try:
        asyncio.run(main())
    except Exception as e:
        logger.error(f"Error: {e}")

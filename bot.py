from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from tenacity import retry, stop_after_attempt, wait_fixed
import logging

# Your Bot Token
TOKEN = "7327073775:AAHS77p3lmuj9iMUMTbBcZ7iq6xakBzR"

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Retry the main bot loop in case of failure
@retry(stop=stop_after_attempt(5), wait=wait_fixed(2))
async def main():
    # Create the application instance
    application = Application.builder().token(TOKEN).build()

    # Initialize the application
    await application.initialize()

    # Define the command handlers
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        welcome_message = """
🗣️ Inquiry / سؤال - https://t.me/+2O18lpzpF_ZiZjY1 

📢 Official Channel / القناة الرسمية  - https://t.me/+2O18lpzpF_ZiZjY1

🛒 Purchase Now / شراء الآن  - https://t.me/Thesqd
        """
        await update.message.reply_text(welcome_message)

    async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("This is the help section. Contact support if needed.")

    # Add command handlers to the application
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Run the bot with polling
    await application.run_polling()

    # Shutdown the application after completion
    await application.shutdown()

# Run the bot
if __name__ == "__main__":
    try:
        import asyncio
        asyncio.run(main())
    except Exception as e:
        logger.error(f"An error occurred: {e}")

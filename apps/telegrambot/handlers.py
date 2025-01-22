from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") # Replace with your bot token

class TelegramHandler:
    def __init__(self):
        # Initialize the bot application
        self.app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

        # Register command and message handlers
        self.app.add_handler(CommandHandler('start', self.start))
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))

    async def process_update(self, data):
        """Process incoming update and return a response."""
        try:
            # Convert raw data to an Update object
            update = Update.de_json(data, self.app.bot)
            # Process the update using the application
            await self.app.process_update(update)
            return {'status': 'success'}
        except Exception as e:
            # Handle any exceptions
            return {'error': str(e)}

    async def start(self, update: Update, context):
        """Handle /start command."""
        await update.message.reply_text("Welcome to the bot! How can I help you?")

    async def handle_message(self, update: Update, context):
        """Handle text messages."""
        await update.message.reply_text(f'You said: {update.message.text}')
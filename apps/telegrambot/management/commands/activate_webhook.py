import asyncio
import logging
from django.core.management.base import BaseCommand
from apps.telegrambot.webhook import main  # Import the async main function

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Starts the Telegram bot and sets up the webhook"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Starting the Telegram bot..."))

        try:
            asyncio.run(main())  # Run the async function
        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING("Bot stopped by user."))
        except Exception as e:
            logger.error(f"Error starting bot: {e}")
            self.stdout.write(self.style.ERROR(f"Error: {e}"))

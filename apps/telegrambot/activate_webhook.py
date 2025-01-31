import asyncio
import json
import logging
from dataclasses import dataclass
from uuid import uuid4
import os

 # Adjust this path if needed


import uvicorn
from django.conf import settings
from django.core.asgi import get_asgi_application
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.urls import path
import os
from dotenv import load_dotenv

from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CallbackContext,
    ConversationHandler,
    ContextTypes,
    ExtBot,
    TypeHandler,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler,
)

from apps.telegrambot.handlers import (
    start,
    native_language,
    language_to_learn,
    language_knowlege_level,
    LANGUAGE_TO_LEARN,
    CONTINUE,
    ENGLISH_KNOWLEGE_LEVEL,
    unknown,
)

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_BOT_CHAT_ID = os.getenv("TELEGRAM_BOT_CHAT_ID")
PUBLIC_URL = "https://40e9-83-250-15-222.ngrok-free.app"


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


# Configuration Constants
URL = PUBLIC_URL
ADMIN_CHAT_ID = TELEGRAM_BOT_CHAT_ID
PORT = 8000
TOKEN = f"{TELEGRAM_BOT_TOKEN}"  # nosec B105


@dataclass
class WebhookUpdate:
    """Simple dataclass to wrap a custom update type"""

    user_id: int
    payload: str


class CustomContext(CallbackContext[ExtBot, dict, dict, dict]):
    """
    Custom CallbackContext class that makes `user_data` available for updates of type
    `WebhookUpdate`.
    """

    @classmethod
    def from_update(
        cls,
        update: object,
        application: "Application",
    ) -> "CustomContext":
        if isinstance(update, WebhookUpdate):
            return cls(application=application, user_id=update.user_id)
        return super().from_update(update, application)


async def webhook_update(update: WebhookUpdate, context: CustomContext) -> None:
    """Handle custom updates."""
    chat_member = await context.bot.get_chat_member(
        chat_id=update.user_id, user_id=update.user_id
    )
    payloads = context.user_data.setdefault("payloads", [])
    payloads.append(update.payload)
    combined_payloads = "</code>\n• <code>".join(payloads)
    text = (
        f"The user {chat_member.user.mention_html()} has sent a new payload. "
        f"So far they have sent the following payloads: \n\n• <code>{combined_payloads}</code>"
    )
    await context.bot.send_message(
        chat_id=ADMIN_CHAT_ID, text=text, parse_mode=ParseMode.HTML
    )


async def telegram(request: HttpRequest) -> HttpResponse:
    """Handle incoming Telegram updates by putting them into the `update_queue`"""
    await ptb_application.update_queue.put(
        Update.de_json(data=json.loads(request.body), bot=ptb_application.bot)
    )
    return HttpResponse()


async def custom_updates(request: HttpRequest) -> HttpResponse:
    """
    Handle incoming webhook updates by also putting them into the `update_queue` if
    the required parameters were passed correctly.
    """
    try:
        user_id = int(request.GET["user_id"])
        payload = request.GET["payload"]
    except KeyError:
        return HttpResponseBadRequest(
            "Please pass both `user_id` and `payload` as query parameters.",
        )
    except ValueError:
        return HttpResponseBadRequest("The `user_id` must be a string!")

    await ptb_application.update_queue.put(
        WebhookUpdate(user_id=user_id, payload=payload)
    )
    # Handle the update with the Application
    return HttpResponse()


# Set up the application and web server
context_types = ContextTypes(context=CustomContext)
ptb_application = (
    Application.builder()
    .token(TOKEN)
    .updater(None)
    .context_types(context_types)
    .build()
)

# register handlers
ptb_application.add_handler(TypeHandler(type=WebhookUpdate, callback=webhook_update))
conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        CONTINUE: [CallbackQueryHandler(native_language)],
        LANGUAGE_TO_LEARN: [CallbackQueryHandler(language_to_learn)],
        ENGLISH_KNOWLEGE_LEVEL: [CallbackQueryHandler(language_knowlege_level)],
    },
    fallbacks=[MessageHandler(filters.TEXT, unknown)],
)
ptb_application.add_handler(conv_handler)
ptb_application.add_handler(CommandHandler("start", start))


urlpatterns = [
    path("telegram", telegram, name="Telegram updates"),
    path("submitpayload", custom_updates, name="custom updates"),
]


settings.configure(ROOT_URLCONF=__name__, SECRET_KEY=uuid4().hex)


async def main() -> None:
    """Finalize configuration and run the applications."""
    webserver = uvicorn.Server(
        config=uvicorn.Config(
            app=get_asgi_application(),
            port=PORT,
            use_colors=False,
            host="127.0.0.1",
        )
    )

    # Pass webhook settings to telegram
    await ptb_application.bot.set_webhook(
        url=f"{URL}/telegram", allowed_updates=Update.ALL_TYPES
    )

    # Run application and webserver together
    async with ptb_application:
        await ptb_application.start()
        await webserver.serve()
        await ptb_application.stop()


if __name__ == "__main__":
    asyncio.run(main())

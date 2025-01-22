from django.http import JsonResponse,HttpResponse

from django.views import View
import requests
import json
from dotenv import load_dotenv
import os
from .handlers import TelegramHandler  # Import your handler logic


class TelegramBotView(View):
    async def post(self, request, *args, **kwargs):
        try:
            # Parse incoming JSON request
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        # Delegate handling to the TelegramHandler
        handler = TelegramHandler()
        response = await handler.process_update(data)
        return JsonResponse(response)
  

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_PUBLIC_URL='https://e207-2a02-aa1-1056-bcde-425-b6ec-6e8-b8a6.ngrok-free.app/'
TELEGRAM_BOT_API = os.getenv("TELEGRAM_BOT_API")

def setwebhook(request):
  response = requests.post(f"{TELEGRAM_BOT_API}setWebhook?url={TELEGRAM_PUBLIC_URL}telegram/webhook/").json()
  return HttpResponse(f"{response}")

def delete_webhook(request):
  response = requests.post(f"{TELEGRAM_BOT_API}setWebhook?url=").json()
  return HttpResponse(f"{response}")
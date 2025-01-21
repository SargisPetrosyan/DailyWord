import json
import requests
from django.http import HttpResponse,JsonResponse
from django.views import View

from .handlers import starthandler,getwordhandler


class TelegramBotHandler(View):
  async def post(self, request,*args, **kwargs):
    try:
      data = json.loads(request.body)
    except json.JSONDecodeError:
      return JsonResponse({'error': 'Invalid JSON'}, status=400)

    event_type = requests.get('event')

    event_handlers = {
      'start':starthandler(),
      'get_word':getwordhandler(),
  }
    handler = event_handlers.get(event_type)

    if handler:
      await handler.handle(data)
      return JsonResponse({'status:''success'}, status=200)
    
    else:
      return JsonResponse({'error':"Unknown event type"}, status=400)
    

TELEGRAM_API_URL = "https://api.telegram.org/bot7210222575:AAFMzyzx6-6tCn3nlqlxo90iinZc5UUOLiQ/"
TELEGRAM_PUBLIC_URL='https://4cf6-83-250-15-222.ngrok-free.app/'


def setwebhook(request):
  response = requests.post(f"{TELEGRAM_API_URL}setWebhook?url={TELEGRAM_PUBLIC_URL}getpost/").json()
  return HttpResponse(f"{response}")

def delete_webhook(request):
  response = requests.post(f"{TELEGRAM_API_URL}setWebhook?url=").json()
  return HttpResponse(f"{response}")
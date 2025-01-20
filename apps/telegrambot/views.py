import json
import requests
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
import os


load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_API_URL = os.getenv("TELEGRAM_API_URL")
TELEGRAM_PUBLIC_URL = os.getenv("TELEGRAM_PUBLIC_URL")
TELEGRAM_WEBHOOK_URL = os.getenv("TELEGRAM_WEBHOOK_URL")

@csrf_exempt
def telegram_bot(request):
  if request.method == 'POST':
    update = json.loads(request.body.decode('utf-8'))
    handle_update(update)
    return HttpResponse('ok')
  else:
    return HttpResponseBadRequest('Bad Request')

def handle_update(update):
  chat_id = update['message']['chat']['id']
  text = update['message']['text']
  send_message("sendMessage", {
    'chat_id': chat_id,
    'text': f'you said {text}'
  })


def send_message(method, data):
  return requests.post(TELEGRAM_API_URL + method, data)


def setwebhook(request):
  response = requests.post(TELEGRAM_WEBHOOK_URL).json()
  return HttpResponse(f"{response}")
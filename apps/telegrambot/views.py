import json
import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_API_URL = os.getenv("TELEGRAM_API_URL")
TELEGRAM_PUBLIC_URL = os.getenv("TELEGRAM_PUBLIC_URL")

@csrf_exempt
def telegram_bot(request):
  if request.method == 'POST':
    message = json.loads(request.body.decode('utf-8'))
    chat_id = message['message']['chat']['id']
    text = message['message']['text']
    send_message("sendMessage", {
      'chat_id': f'your message {text}'
    })
  return HttpResponse('ok')

def send_message(method, data):
  return requests.post(TELEGRAM_API_URL+ method, data)

def setwebhook(request):
  response = requests.post(TELEGRAM_API_URL+ "setWebhook?url=" + TELEGRAM_PUBLIC_URL).json()
  return HttpResponse(f"{response}")
from .views import TelegramBotView,delete_webhook,setwebhook
from django.urls import path

urlpatterns = [
  path('webhook/', TelegramBotView.as_view(), name='telegram_bot'),
  path('deletewebhook/', delete_webhook, name='delete_webhook'),
  path('setwebhook/', setwebhook, name='setwebhook'),
]
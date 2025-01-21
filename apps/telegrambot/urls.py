from . import views
from django.urls import path

urlpatterns = [
  path('getpost/', views.TelegramBotHandler.as_view(), name='telegram_bot'),
  path('deletewebhook/', views.delete_webhook, name='delete_webhook'),
  path('setwebhook/', views.setwebhook, name='setwebhook'),
]
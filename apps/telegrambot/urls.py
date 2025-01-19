from . import views
from django.urls import path

urlpatterns = [
  path('getpost/', views.telegram_bot, name='telegram_bot'),
  path('setwebhook/', views.setwebhook, name='setwebhook'),
]
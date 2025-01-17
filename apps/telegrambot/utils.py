from dotenv import find_dotenv, load_dotenv
from telegram import Update
import logging
import os

#import Telegarm token from .env
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

#loging configuration 
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
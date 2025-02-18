import aiohttp

from .validation import WordValidation

import logging

from googletrans import Translator

import os
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

BASE_URL = os.getenv("FREEDICTIONARY_API_URL")


class GetWord:
    @staticmethod
    async def fetch_data(url: str, params: dict) -> dict:
        """Helper function to make a GET request and return the response data."""    
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                try:
                    if response.status == 200:
                        await WordValidation.validate_json_create_dict(response)
                        

                    else:
                        logger.warning(f"Error: {response.status}")
                        return(f"Error: {response.status}")
                except:
                    pass
                
    @staticmethod
    async def get_word_example(word:str):
        

    
class TranslateWord:
    @staticmethod
    async def translate_word(word: str) -> str:
        translator = Translator()
        result = await translator.translate(text=word, dest='en', src='ru')
        return result.text

    
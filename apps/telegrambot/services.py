from doctest import Example
from apps.telegrambot.repositories import UserRepository

from telegram import Update

from .requests import GetWord, TranslateWord

from typing import Optional




class UserService:
    @staticmethod
    async def create_user(user_chat_id: int, username: str, language_code: str):
        await UserRepository.create_user(
            user_chat_id=user_chat_id,
            username=username,
            language_code=language_code,
        )

    @staticmethod
    async def user_exist(user_chat_id: int) -> bool:
        return await UserRepository.user_exists(user_chat_id=user_chat_id)

    @staticmethod
    async def set_native_language(user_chat_id: int, native_language: str) -> None:
        await UserRepository.set_user_native_language(
            user_chat_id=user_chat_id, native_language=native_language
        )

    @staticmethod
    async def set_language_to_learn(user_chat_id: int, language_to_learn: str) -> None:
        await UserRepository.set_user_language_to_learn(
            user_chat_id=user_chat_id, language_to_learn=language_to_learn
        )

    @staticmethod
    async def set_user_language_knowledge_level(
        user_chat_id: int, language_knowledge_level: str
    ) -> None:
        await UserRepository.set_user_language_knowledge_level(
            user_chat_id=user_chat_id, language_knowledge_level=language_knowledge_level
        )
        
class QueryType:
    @staticmethod   
    async def check_query_type(update: Update) -> None:
        if update.callback_query:
            query = update.callback_query
            await query.answer()
        elif update.message:
            # await update.message
            pass
        
    @staticmethod    
    async def reply_query(update: Update, reply_text: str, reply_markup: Optional[list]= None) -> None:
        if update.callback_query:  # Button click -> Edit message
            await update.callback_query.edit_message_text(
                text=reply_text, reply_markup=reply_markup
                )
        elif update.message:  # Command -> Send new message
            await update.message.reply_text(text=reply_text, reply_markup=reply_markup)
            
class GetWordServices:
    @staticmethod
    async def get_word_definition_service(word: str) -> str:
        word_data = await GetWord.get_word_definitions(word=word)
        definition = word_data[0]["text"]
        return definition
    
    @staticmethod    
    async def get_word_example(word: str, top_example: bool) -> str:
        word_data = await GetWord.get_word_examples(word=word, top_example=top_example)
        print(word_data)    
        example = word_data['examples'][0]['text']
        return example
    
class TranslateWordService:
    @staticmethod
    async def translate_word(word: str) -> str:
        result = await TranslateWord.translate_word(word=word)
        return result
    

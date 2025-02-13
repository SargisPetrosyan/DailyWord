from apps.telegrambot.repositories import UserRepasitory

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)



class UserService:
    @staticmethod
    async def create_user(user_chat_id: int, username: str, language_code: str):
        await UserRepasitory.create_user(
            user_chat_id=user_chat_id,
            username=username,
            language_code=language_code,
        )

    @staticmethod
    async def user_exist(user_chat_id: int) -> bool:
        return await UserRepasitory.user_exists(user_chat_id=user_chat_id)

    @staticmethod
    async def set_native_language(user_chat_id: int, native_language: str) -> None:
        await UserRepasitory.set_user_native_language(
            user_chat_id=user_chat_id, native_language=native_language
        )

    @staticmethod
    async def set_language_to_learn(user_chat_id: int, language_to_learn: str) -> None:
        await UserRepasitory.set_user_language_to_learn(
            user_chat_id=user_chat_id, language_to_learn=language_to_learn
        )

    @staticmethod
    async def set_user_language_knowledge_level(
        user_chat_id: int, language_knowledge_level: str
    ) -> None:
        await UserRepasitory.set_user_language_knowledge_level(
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
    async def reply_query(update: Update, reply_text: str, reply_markup: list) -> None:
        if update.callback_query:  # Button click -> Edit message
            await update.callback_query.edit_message_text(
                text=reply_text, reply_markup=reply_markup
                )
        elif update.message:  # Command -> Send new message
            await update.message.reply_text(text=reply_text, reply_markup=reply_markup)
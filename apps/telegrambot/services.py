from apps.telegrambot.repositories import UserRepasitory

async def create_user( user_chat_id,username,language_code,):
    await UserRepasitory.create_user(
        user_chat_id=user_chat_id,
        username=username,
        language_code=language_code,
)

    
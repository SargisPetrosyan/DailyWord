from apps.telegrambot.repositories import UserRepasitory


async def create_user(user_chat_id: int, username: str, language_code: str):
    await UserRepasitory.create_user(
        user_chat_id=user_chat_id,
        username=username,
        language_code=language_code,
    )


async def user_exist(user_chat_id: int) -> bool:
    return await UserRepasitory.user_exists(user_chat_id=user_chat_id)


async def set_native_language(user_chat_id: int, native_language: str) -> None:
    await UserRepasitory.set_user_native_language(
        user_chat_id=user_chat_id, native_language=native_language
    )


async def set_language_to_learn(user_chat_id: int, language_to_learn: str) -> None:
    await UserRepasitory.set_user_language_to_learn(
        user_chat_id=user_chat_id, language_to_learn=language_to_learn
    )


async def set_user_language_knowlege_level(
    user_chat_id: int, language_knowlege_level: str
) -> None:
    await UserRepasitory.set_user_language_knowlege_level(
        user_chat_id=user_chat_id, language_knowlege_level=language_knowlege_level
    )

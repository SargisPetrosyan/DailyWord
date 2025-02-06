from apps.telegrambot.models import User


class UserRepasitory:
    @staticmethod
    async def create_user(
        user_chat_id: int,
        username: str,
        language_code: str,
        native_language: str = None,
        language_to_learn: str = None,
        language_knowlege_level: str = None,
    ) -> User:
        user = User(
            user_chat_id=user_chat_id,
            username=username,
            language_code=language_code,
            native_language=native_language,
            language_to_learn=language_to_learn,
            language_knowlege_level=language_knowlege_level,
        )
        await user.asave()
        return user

    @staticmethod
    async def user_exists(user_chat_id: int) -> bool:
        return await User.objects.filter(user_chat_id=user_chat_id).aexists()

    @staticmethod
    async def get_user_by_chat_id(user_chat_id: int) -> int:
        return await User.objects.aget(user_chat_id=user_chat_id)

    @staticmethod
    async def set_user_native_language(user_chat_id: int, native_language: str) -> None:
        user = await User.objects.aget(user_chat_id=user_chat_id)
        user.native_language = native_language
        await user.asave()

    @staticmethod
    async def set_user_language_to_learn(
        user_chat_id: int, language_to_learn: str
    ) -> None:
        user = await User.objects.aget(user_chat_id=user_chat_id)
        user.language_to_learn = language_to_learn
        await user.asave()

    @staticmethod
    async def set_user_language_knowlege_level(
        user_chat_id: int, language_knowlege_level: str
    ) -> None:
        user = await User.objects.aget(user_chat_id=user_chat_id)
        user.language_knowlege_level = language_knowlege_level
        await user.asave()

    # @staticmethod
    # async def get_user_language_to_learn(language_to_learn):
    #      return User.objects.filter(native_language=language_to_learn)

    # @staticmethod
    # @user_exists_decorator
    # async def get_user_updated_at(updated_at):
    #      return User.objects.filter(updated_at=updated_at).all()

    # @staticmethod

    # async def get_user_created_at(created_at):
    #      return User.objects.filter(created_at=created_at).all()

    # @staticmethod

    # async def delete_user(user_chat_id):
    #      User.objects.filter(user_chat_id=user_chat_id).delete()

    # @staticmethod
    # async def update_native_language(user_chat_id,new_native_language):

    #     user= UserRepasitory.get_user_by_id(user_chat_id)
    #     if user:
    #         user.native_language =new_native_language
    #         user.save()
    #         return user  # Return the updated user object
    #     else:
    #         raise ValueError(f"User with chat ID {user_chat_id} not found.")

    # @staticmethod
    # async def update_language_to_learn(user_chat_id,new_learning_language):

    #     user= UserRepasitory.get_user_by_id(user_chat_id)
    #     if user:
    #         user.language_to_learn =new_learning_language
    #         user.save()
    #         return user  # Return the updated user object
    #     else:
    #         raise ValueError(f"User with chat ID {user_chat_id} not found.")

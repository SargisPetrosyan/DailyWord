from apps.telegrambot.models import User
import asyncio


class UserRepasitory:
    @staticmethod
    async def create_user(user_chat_id, 
                    username, 
                    language_code, 
                    native_language=None, 
                    language_to_learn=None,):
        
        user = User(
            user_chat_id=user_chat_id,
            username=username,
            language_code=language_code,
            native_language=native_language,
            language_to_learn=language_to_learn,
        )
        await user.save()
        return user

    @staticmethod
    async def get_user_by_chat_id(user_chat_id):
        try:
            return await asyncio.wait_for(User.objects.aget(pk=user_chat_id), timeout=5)
        except asyncio.TimeoutError:
            print("Query timed out")
    
    @staticmethod
    async def get_user_native_language(user_chat_id,native_language):
        try:
             user = await asyncio.wait_for(User.objects.filter(pk=native_language).aget(user_chat_id=user_chat_id), timeout=5)
             return user.native_language if user else None
        except asyncio.Timeout:
            print("Query timed out")

        
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

    

    

from telegrambot.models import User
from functools import wraps

#Decoartor
def user_exists_decorator(func):
    @wraps(func)
    async def wrapper(user_chat_id,*args,**kwargs):
        user = await UserRepasitory.get_user_by_id(user_chat_id)
        if not user:
            raise ValueError(f"User with chat ID {user_chat_id} not found")
        return await func(user_chat_id, *args,**kwargs)
    return wrapper

class UserRepasitory:

    @staticmethod
    async def create_user(user_chat_id, 
                    username, 
                    language_code, 
                    native_language, 
                    language_to_learn):
        
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
    @user_exists_decorator
    async def get_user_by_id(user_chat_id):
         return await User.objects.filter(user_chat_id=user_chat_id )
    
    # @staticmethod
    # @user_exists_decorator
    # async def get_user_native_language(user_chat_id,nativ_language):
        
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

    

    

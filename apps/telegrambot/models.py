from django.db import models


class User(models.Model):
    user_chat_id = models.IntegerField(unique=True)
    username = models.CharField(max_length=255)
    language_code = models.CharField(max_length=50)
    native_language = models.CharField(max_length=50, null=True)
    language_to_learn = models.CharField(max_length=50, null=True)
    language_knowledge_level=models.CharField(max_length=50, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    

    def __str__(self):
        return f"name{self.username} chat ID:{self.user_chat_id}"



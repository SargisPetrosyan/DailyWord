import asyncio
import telegram


async def main():
    bot = telegram.Bot("7210222575:AAFMzyzx6-6tCn3nlqlxo90iinZc5UUOLiQ")
    async with bot:
        print(await bot.get_me())


if __name__ == '__main__':
    asyncio.run(main())


""" Update(message=Message("channel_chat_created=False",
"chat=Chat(first_name=""Sargis",
id=5464909067,
"last_name=""Petrosyan",
"type=<ChatType.PRIVATE>)",
date=datetime.datetime(2025,1,28,13,28,6,
"tzinfo=datetime.timezone.utc)",
"delete_chat_photo=False",
entities=(MessageEntity(length=6,
offset=0,
"type=<MessageEntityType.BOT_COMMAND>)",
")",
"from_user=User(first_name=""Sargis",
id=5464909067,
"is_bot=False",
"language_code=""en",
"last_name=""Petrosyan"")",
"group_chat_created=False",
message_id=438,
"supergroup_chat_created=False",
"text=""/start"")",
update_id=752585494)"""
import asyncio
import telegram


async def main():
    bot = telegram.Bot("7210222575:AAFMzyzx6-6tCn3nlqlxo90iinZc5UUOLiQ")
    async with bot:
        print(await bot.get_me())


if __name__ == '__main__':
    asyncio.run(main())
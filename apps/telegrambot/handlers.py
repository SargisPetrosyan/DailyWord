from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from apps.telegrambot.services import create_user

from telegram.ext import (
    ContextTypes,
    ConversationHandler,
)

languages = [
    ["English", "Spanish", "French"],
    ["Russian", "Chinese", "Hindi"],
    ["Portuguese", "Japanese", "German"],
]
markup_languages = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(language, callback_data=language.lower())
            for language in row
        ]
        for row in languages
    ]
)

CONTINUE, LANGUAGE_TO_LEARN, ENGLISH_KNOWLEGE_LEVEL = range(3)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start the conversation and ask user for input."""
    await create_user(
        user_chat_id=update.message.chat.id,
        username='Barev',
        language_code=update.message.from_user.language_code,
        )
    
    keyboard = [[InlineKeyboardButton("Continue", callback_data="continue")]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        """🎉 Welcome to Daily Word Bot! 🎉

Your ultimate companion for building your vocabulary, one word at a time (or more)!

                        Here's what you can do:
📚 Pick words from various categories that interest you.
📖 Organize and save words in your personalized, categorized dictionaries.
📅 Get one or multiple words delivered to you every day!
📝 Challenge yourself with quizzes to reinforce your learning.

Let’s make learning fun and exciting! 🥳

Ready to start? Tap continue! 👇
""",
        reply_markup=reply_markup,
    )

    return CONTINUE


async def native_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Handle other cases or log an error

    await update.callback_query.answer()
    await update.callback_query.message.reply_text(
        """Before we start, please select your languages:
        🌐 From: (Your native language)""",
        reply_markup=markup_languages,
    )

    return LANGUAGE_TO_LEARN


async def language_to_learn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.message.reply_text(
        """Now you chose languge that want to learn:
        🌐 To: (language thet want to learn)""",
        reply_markup=markup_languages,
    )

    return ENGLISH_KNOWLEGE_LEVEL


async def language_knowlege_level(update: Update, context: ContextTypes.DEFAULT_TYPE):
    language_level_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Beginner", callback_data="beginner"),
                InlineKeyboardButton("Intermiediate", callback_data="intermiediate"),
                InlineKeyboardButton("Advance", callback_data="advance"),
            ]
        ]
    )
    await update.callback_query.answer()
    await update.callback_query.message.reply_text(
        f""" ✨ You're almost there! ✨

🎯 Please select your English knowledge level:
😊 Don’t worry! The bot will adjust to you,
changing word difficulty based on your progress.

Once you pick your level, we’ll get started! 🚀
    """,
        reply_markup=language_level_markup,
    )
    return ConversationHandler.END


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Sorry, I didn’t understand that. Please choose a valid option."
    )

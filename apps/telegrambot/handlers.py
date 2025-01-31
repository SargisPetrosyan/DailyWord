from telegram import (Update,InlineKeyboardButton,InlineKeyboardMarkup,)
from telegram.ext import (ContextTypes,ConversationHandler,)
from apps.telegrambot.services import (
    create_user,
    user_exist,
    set_native_language,
    set_language_to_learn,
    set_user_language_knowlege_level,
)

languages = [
    ["English", "Spanish", "French"],
    ["Russian", "Chinese", "Hindi"],
    ["Portuguese", "Japanese", "German"],
]
markup_languages = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('English', callback_data='en'),
            InlineKeyboardButton('Spanish', callback_data='es'),
            InlineKeyboardButton('French', callback_data='fr') 
        ],
        [
            InlineKeyboardButton('Russian', callback_data='ru'),
            InlineKeyboardButton('Chinese', callback_data='zh'),
            InlineKeyboardButton('Hindi', callback_data='hi') 
        ],
        [
            InlineKeyboardButton('Portuguese ', callback_data='pt'),
            InlineKeyboardButton('Japanese ', callback_data='ja'),
            InlineKeyboardButton('German ', callback_data='de') 
        ]
    ]
)

CONTINUE, LANGUAGE_TO_LEARN, ENGLISH_KNOWLEGE_LEVEL = range(3)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start the conversation and ask user for input."""
    user = await user_exist(user_chat_id=update.message.chat.id) #5464909067
    if not user:
        await create_user(
            user_chat_id=update.message.chat.id,
            username=update.message.from_user.first_name,
            language_code=update.message.from_user.language_code,
            )
    
    else:
        pass
    
    keyboard = [[InlineKeyboardButton("Continue", callback_data="continue")]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        f"""🎉 Welcome {str(update.message.from_user.first_name)} to Daily Word Bot ! 🎉

Your ultimate companion for building your vocabulary, one word at a time (or more)!

📚 Pick words from various categories that interest you.
📖 Save and organize words in your personalized dictionaries.
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
    await set_native_language(user_chat_id=update.callback_query.message.chat.id, native_language=update.callback_query.data)
    return LANGUAGE_TO_LEARN


async def language_to_learn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.message.reply_text(
        """Now you chose languge that want to learn:
        🌐 To: (language thet want to learn)""",
        reply_markup=markup_languages,
    )
    await set_language_to_learn(user_chat_id=update.callback_query.message.chat.id, language_to_learn=update.callback_query.data)

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
    await set_user_language_knowlege_level(user_chat_id=update.callback_query.message.chat.id,language_knowlege_level=update.callback_query.data)
    return ConversationHandler.END


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Sorry, I didn’t understand that. Please choose a valid option."
    )

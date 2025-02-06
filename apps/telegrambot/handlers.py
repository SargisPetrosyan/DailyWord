from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram.ext import (
    ContextTypes,
    ConversationHandler,
)

from apps.telegrambot.services import (
    create_user,
    user_exist,
    set_native_language,
    set_language_to_learn,
    set_user_language_knowlege_level,
)

import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# Stages
MENU_ROUTES, END_MENU_ROUTES = range(2)
# Callback data
(   
    DAILY_WORD, 
    VOCABULARY,
    MENU, 
    KNOWLEGE_LEVEL, 
    NATIVE_LANGUAGE,
    LANGUAGE_TO_LEARN,
    SETTINGS,
    HELP,
    SEARCH,
    ARCHIVE,
    QUIZ,  
) = range(11)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Send message on `/start`."""
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    keyboard = [
        [
            InlineKeyboardButton("📆 Word of Day", callback_data=str(DAILY_WORD)),
            InlineKeyboardButton("📖 Vocabulary", callback_data=str(VOCABULARY)),
        ],
        [
            InlineKeyboardButton("🎯 Quiz", callback_data=str("quiz")),
            InlineKeyboardButton("🔍 Search Word", callback_data=str("search_word")),
        ],
        [
            InlineKeyboardButton("🗂️ Archive", callback_data=str("archive")),
            InlineKeyboardButton("❓ Help", callback_data=str("help")),
        ],
        [
            InlineKeyboardButton("⚙️ Settings", callback_data=str("settings")),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    await update.message.reply_text(
text="""Hey!👋 Welcome to the Daily Word Bot! 🌟

You can find words and their descriptions, set up a daily word, 
select categories, save them, and learn them. 📚✨

Use the menu below for all options! ⬇️
For assistance, select /help """,
reply_markup=reply_markup)
    # Tell ConversationHandler that we're in state `FIRST` now
    return MENU_ROUTES



async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Send message on `/menu`."""
    query = update.callback_query
    # logger.info("User %s started the conversation.", query.first_name)
    keyboard = [
        [
            InlineKeyboardButton("📆 Word of Day", callback_data=str(DAILY_WORD)),
            InlineKeyboardButton("📖 Vocabulary", callback_data=str(VOCABULARY)),
        ],
        [
            InlineKeyboardButton("🎯 Quiz", callback_data=str(QUIZ)),
            InlineKeyboardButton("🔍 Search Word", callback_data=str(SEARCH)),
        ],
        [
            InlineKeyboardButton("🗂️ Archive", callback_data=str(ARCHIVE)),
            InlineKeyboardButton("❓ Help", callback_data=str(HELP)),
        ],
        [
            InlineKeyboardButton("⚙️ Settings", callback_data=str(SETTINGS)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    await query.edit_message_text(
text="""Hey!👋 Welcome to the Daily Word Bot! 🌟

You can find words and their descriptions, set up a daily word, 
select categories, save them, and learn them. 📚✨

Use the menu below for all options! ⬇️
For assistance, select /help """,
reply_markup=reply_markup)
    # Tell ConversationHandler that we're in state `FIRST` now
    return MENU_ROUTES


async def daily_word(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
            [
                InlineKeyboardButton("🏷️ Categories", callback_data=str("categories")),
                InlineKeyboardButton("🔢 Word Quentity", callback_data=str("word_quentity")),
            ],
            [
                InlineKeyboardButton("<< Menu", callback_data=str(MENU)),
            ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="📆 hear you can change Daily Word settings", reply_markup=reply_markup
    )
    return MENU_ROUTES


async def settings(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
            [
                InlineKeyboardButton("🔠 Native Language", callback_data=str(NATIVE_LANGUAGE)),
                InlineKeyboardButton("🌐 Language To Learn", callback_data=str(LANGUAGE_TO_LEARN)),
            ],
            [
                InlineKeyboardButton("<< Menu", callback_data=str(MENU)),
                InlineKeyboardButton("🎓 Knowlage Level", callback_data=str(KNOWLEGE_LEVEL)),
            ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="⚙️ settings", reply_markup=reply_markup
    )
    return MENU_ROUTES

async def vocabulary(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
            [
                InlineKeyboardButton(" All Words", callback_data=str(NATIVE_LANGUAGE)),
                InlineKeyboardButton(" Programming", callback_data=str(LANGUAGE_TO_LEARN)),
            ],
            [
                InlineKeyboardButton(" Medicine", callback_data=str(NATIVE_LANGUAGE)),
                InlineKeyboardButton(" Tech", callback_data=str(LANGUAGE_TO_LEARN)),
            ],
            [
                InlineKeyboardButton("<< Menu", callback_data=str(MENU)),
                InlineKeyboardButton("🎓 Science", callback_data=str(KNOWLEGE_LEVEL)),
            ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="⚙️ settings", reply_markup=reply_markup
    )
    return MENU_ROUTES

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
            [
                InlineKeyboardButton("<< Menu", callback_data=str(MENU)),
            ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="❓ hear should be help information", reply_markup=reply_markup
    )
    return MENU_ROUTES

async def search_word(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
            [
                InlineKeyboardButton("<< Menu", callback_data=str(MENU)),
            ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="🔍 hear should be word search logic", reply_markup=reply_markup
    )
    return MENU_ROUTES

async def archive(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
            [
                InlineKeyboardButton("<< Menu", callback_data=str(MENU)),
            ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="🗂️ hear should be word archive logic", reply_markup=reply_markup
    )
    return MENU_ROUTES

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
            [
                InlineKeyboardButton("<< Menu", callback_data=str(MENU)),
            ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="🎯 hear should be quiz logic", reply_markup=reply_markup
    )
    return MENU_ROUTES


async def native_language(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    pass

async def knowlege_level(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    pass

async def language_to_learn(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    pass

async def categories(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    pass







# async def three(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     """Show new choice of buttons. This is the end point of the conversation."""
#     query = update.callback_query
#     await query.answer()
#     keyboard = [
#         [
#             InlineKeyboardButton("Yes, let's do it again!", callback_data=str(ONE)),
#             InlineKeyboardButton("Nah, I've had enough ...", callback_data=str(TWO)),
#         ]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     await query.edit_message_text(
#         text="Third CallbackQueryHandler. Do want to start over?", reply_markup=reply_markup
#     )
#     # Transfer to conversation state `SECOND`
#     return END_ROUTES


# async def four(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     """Show new choice of buttons"""
#     query = update.callback_query
#     await query.answer()
#     keyboard = [
#         [
#             InlineKeyboardButton("2", callback_data=str(TWO)),
#             InlineKeyboardButton("3", callback_data=str(THREE)),
#         ]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     await query.edit_message_text(
#         text="Fourth CallbackQueryHandler, Choose a route", reply_markup=reply_markup
#     )
#     return START_ROUTES


# async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     """Returns `ConversationHandler.END`, which tells the
#     ConversationHandler that the conversation is over.
#     """
#     query = update.callback_query
#     await query.answer()
#     await query.edit_message_text(text="See you next time!")
#     return ConversationHandler.END







# languages = [
#     ["English", "Spanish", "French"],
#     ["Russian", "Chinese", "Hindi"],
#     ["Portuguese", "Japanese", "German"],
# ]
# markup_languages = InlineKeyboardMarkup(
#     [
#         [
#             InlineKeyboardButton("English", callback_data="en"),
#             InlineKeyboardButton("Spanish", callback_data="es"),
#             InlineKeyboardButton("French", callback_data="fr"),
#         ],
#         [
#             InlineKeyboardButton("Russian", callback_data="ru"),
#             InlineKeyboardButton("Chinese", callback_data="zh"),
#             InlineKeyboardButton("Hindi", callback_data="hi"),
#         ],
#         [
#             InlineKeyboardButton("Portuguese ", callback_data="pt"),
#             InlineKeyboardButton("Japanese ", callback_data="ja"),
#             InlineKeyboardButton("German ", callback_data="de"),
#         ],
#     ]
# )

# CONTINUE, LANGUAGE_TO_LEARN, ENGLISH_KNOWLEGE_LEVEL = range(3)


# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """Start the conversation and ask user for input."""
#     user = await user_exist(user_chat_id=update.message.chat.id)
#     if not user:
#         await create_user(
#             user_chat_id=update.message.chat.id,
#             username=update.message.from_user.first_name,
#             language_code=update.message.from_user.language_code,
#         )

#     else:
#         pass

#     keyboard = [[InlineKeyboardButton("Continue", callback_data="continue")]]

#     reply_markup = InlineKeyboardMarkup(keyboard)
#     await update.message.reply_text(
#         f"""🎉 Welcome {str(update.message.from_user.first_name)} to Daily Word Bot ! 🎉

# Your ultimate companion for building your vocabulary, one word at a time (or more)!

# 📚 Pick words from various categories that interest you.
# 📖 Save and organize words in your personalized dictionaries.
# 📅 Get one or multiple words delivered to you every day!
# 📝 Challenge yourself with quizzes to reinforce your learning.

# Let’s make learning fun and exciting! 🥳

# Ready to start? Tap continue! 👇
# """,
#         reply_markup=reply_markup,
#     )

#     return CONTINUE


# async def native_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     # Handle other cases or log an error

#     await update.callback_query.answer()
#     await update.callback_query.message.reply_text(
#         """Before we start, please select your languages:
#         🌐 From: (Your native language)""",
#         reply_markup=markup_languages,
#     )
    
#     await set_native_language(
#         user_chat_id=update.callback_query.message.chat.id,
#         native_language=update.callback_query.data,
#     )
#     return LANGUAGE_TO_LEARN


# async def language_to_learn(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.callback_query.message.reply_text(
#         """Now you chose languge that want to learn:
#         🌐 To: (language thet want to learn)""",
#         reply_markup=markup_languages,
#     )
#     await set_language_to_learn(
#         user_chat_id=update.callback_query.message.chat.id,
#         language_to_learn=update.callback_query.data,
#     )

#     return ENGLISH_KNOWLEGE_LEVEL


# async def language_knowlege_level(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     language_level_markup = InlineKeyboardMarkup(
#         [
#             [
#                 InlineKeyboardButton("Beginner", callback_data="beginner"),
#                 InlineKeyboardButton("Intermiediate", callback_data="intermiediate"),
#                 InlineKeyboardButton("Advance", callback_data="advance"),
#             ]
#         ]
#     )
#     await update.callback_query.answer()
#     await update.callback_query.message.reply_text(
#         f""" ✨ You're almost there! ✨

# 🎯 Please select your English knowledge level:
# 😊 Don’t worry! The bot will adjust to you,
# changing word difficulty based on your progress.

# Once you pick your level, we’ll get started! 🚀
#     """,
#         reply_markup=language_level_markup,
#     )
#     await set_user_language_knowlege_level(
#         user_chat_id=update.callback_query.message.chat.id,
#         language_knowlege_level=update.callback_query.data,
#     )
#     return ConversationHandler.END


# async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         "Sorry, I didn’t understand that. Please choose a valid option."
#     )

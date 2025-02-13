# python-telegram-bot lib and telegam.
from telegram import Update,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import ContextTypes

# Telegram messages and markups for buttons.
from .messages import (
    WELCOME_MESSAGE_TEXT,
    NATIVE_LANGUAGE_TEXT,
    LANGUAGE_KNOWLEDGE_LEVEL_TEXT,
    LANGUAGE_TO_LEARN_TEXT,
    UNKNOWN_MESSAGE_TEXT,
    TO_MENU_TEXT,
    MAIN_MENU_TEXT,
    DAILY_WORD_SETTINGS_TEXT,
    SETTINGS_TEXT,
    VOCABULARY_TEXT,
    SEARCH_WORD_TEXT,
    ARCHIVE_TEXT,
    QUIZ_TEXT 
)

(
LANGUAGE_TO_LEARN, 
ENGLISH_KNOWLEDGE_LEVEL,
FINISH_REGISTRATION,
CONTINUE,
MENU_ROUTES,
DAILY_WORD, 
VOCABULARY,
MENU, 
KNOWLEDGE_LEVEL, 
NATIVE_LANGUAGE,
LANGUAGE_TO_LEARN,
SETTINGS,
HELP,
SEARCH,
ARCHIVE,
QUIZ
) = map(chr, range(16))

from telegram import Update

#telegram services
from apps.telegrambot.services import QueryType,GetWordServices

import logging

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# Callback data


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Start the conversation with a welcome message and ask user to continue."""
    
    # Define the inline keyboard with a "Continue" button
    keyboard = [[InlineKeyboardButton("Continue", callback_data="continue")]]
    start_markup = InlineKeyboardMarkup(keyboard)
    
    # Format the welcome message with the user's first name
    message = WELCOME_MESSAGE_TEXT.format(first_name = update.message.from_user.first_name)
    
    # Send the formatted welcome message along with the inline keyboard
    await update.callback_query.edit_message_text(text=message, reply_markup=start_markup,)
    
    return CONTINUE


async def native_language_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Ask the user to select their native language"""
    
    # Acknowledge the callback query
    await update.callback_query.answer()
     
    native_language_markup: InlineKeyboardMarkup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("English", callback_data="en"),
            InlineKeyboardButton("Spanish", callback_data="es"),
            InlineKeyboardButton("French", callback_data="fr"),
        ],
        [
            InlineKeyboardButton("Russian", callback_data="ru"),
            InlineKeyboardButton("Chinese", callback_data="zh"),
            InlineKeyboardButton("Hindi", callback_data="hi"),
        ],
        [
            InlineKeyboardButton("Portuguese ", callback_data="pt"),
            InlineKeyboardButton("Japanese ", callback_data="ja"),
            InlineKeyboardButton("German ", callback_data="de"),
        ],
    ]
    )
    
    # Prompt user to choose their ative with inline keyboard
    await update.callback_query.edit_message_text(
        text=NATIVE_LANGUAGE_TEXT,
        reply_markup=native_language_markup,
    )

    return LANGUAGE_TO_LEARN


async def language_to_learn_start(update: Update, context: ContextTypes.DEFAULT_TYPE)-> None:
    """Ask the user to select the language they want to learn."""
    language_to_learn: InlineKeyboardMarkup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("English", callback_data="en"),
            InlineKeyboardButton("Spanish", callback_data="es"),
            InlineKeyboardButton("French", callback_data="fr"),
        ],
        [
            InlineKeyboardButton("Russian", callback_data="ru"),
            InlineKeyboardButton("Chinese", callback_data="zh"),
            InlineKeyboardButton("Hindi", callback_data="hi"),
        ],
        [
            InlineKeyboardButton("Portuguese ", callback_data="pt"),
            InlineKeyboardButton("Japanese ", callback_data="ja"),
            InlineKeyboardButton("German ", callback_data="de"),
        ],
    ]
    )
    # Prompt user to choose language to learn with inline keyboard
    await update.callback_query.edit_message_text(
        text=LANGUAGE_TO_LEARN_TEXT, reply_markup=language_to_learn,
    )
    
    return ENGLISH_KNOWLEDGE_LEVEL


async def language_knowledge_level_start(update: Update, context: ContextTypes.DEFAULT_TYPE)-> None:
    """Ask the user to select their language knowledge level"""
    
    # Define the inline keyboard for language levels
    language_level_markup: InlineKeyboardMarkup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Beginner", callback_data="beginner"),
            InlineKeyboardButton("Intermiediate", callback_data="intermiediate"),
            InlineKeyboardButton("Advance", callback_data="advance"),
        ]
    ]
)
    
    await update.callback_query.answer()
    
    # Prompt user to choose their language level with inline keyboard
    await update.callback_query.edit_message_text(
        LANGUAGE_KNOWLEDGE_LEVEL_TEXT, reply_markup=language_level_markup,
    )
    
    return FINISH_REGISTRATION
    

async def to_menu_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Go to menu"""
    
    await update.callback_query.answer()
    
    # Send message with inline keyboard
    await update.callback_query.edit_message_text(
        text = TO_MENU_TEXT,
        reply_markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton("LET'S BEGIN!!", callback_data=MENU)]]
    ),
    )

    return MENU_ROUTES


async def unknown_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """reply UNKNOWN_TEXT command"""
    await update.message.reply_text(UNKNOWN_MESSAGE_TEXT)


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Menu section where all options are visible"""
   
    # check query type.
    await QueryType.check_query_type(update=update)
    
    # Define the main manu inline keyboard markup
    main_menu_markup: InlineKeyboardMarkup = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("📆 Daily Word", callback_data=str(DAILY_WORD)),
                InlineKeyboardButton("📖 Vocabulary", callback_data=str(VOCABULARY)),
            ],
            [
                InlineKeyboardButton("🎯 Quiz ", callback_data=str(QUIZ)),
                InlineKeyboardButton("🔍 Search Word", callback_data=str(SEARCH)),
            ],
            [
                InlineKeyboardButton("🗂️ Archive", callback_data=str(ARCHIVE)),
                InlineKeyboardButton("❓ Help", callback_data=str(HELP)),
            ],
            [
                InlineKeyboardButton("⚙️ Settings", callback_data=str(SETTINGS)),
            ]
    ])
    
    # Send message with text and appended InlineKeyboard
    await QueryType.reply_query(
            update=update, 
            reply_text=MAIN_MENU_TEXT, 
            reply_markup=main_menu_markup
            )
    
    return MENU_ROUTES

async def daily_word(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Daily Word section where you can set up daily word settings"""
    
    # check query type.
    await QueryType.check_query_type(update=update)
    
    # Define the daily word inline keyboard markup
    daily_word_markup: InlineKeyboardMarkup = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("🏷️ Categories", callback_data=str("categories")),
                InlineKeyboardButton("🔢 Word Quentity", callback_data=str("word_quentity")),
            ],
            [
                InlineKeyboardButton("<< Menu", callback_data=str(MENU)),
            ]
        ])
    
    # Send message with text and appended InlineKeyboard
    await QueryType.reply_query(
            update=update, 
            reply_text= DAILY_WORD_SETTINGS_TEXT, 
            reply_markup=daily_word_markup
            )
    
    return MENU_ROUTES

async def settings(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Settings section where you can edit settings"""
   
    # Check query type.
    await QueryType.check_query_type(update)
    
    # Define the settings inline keyboard markup
    settings_markup: InlineKeyboardMarkup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🔠 Native Language", callback_data=str(NATIVE_LANGUAGE)),
                InlineKeyboardButton("🌐 Language To Learn", callback_data=str(LANGUAGE_TO_LEARN)),
            ],
            [
                InlineKeyboardButton("<< Menu", callback_data=str(MENU)),
                InlineKeyboardButton("🎓 Knowledge Level", callback_data=str(KNOWLEDGE_LEVEL)),
            ]
        ]
    )
    
    # Send message with text and appended InlineKeyboard
    await QueryType.reply_query(
        update=update, reply_text=SETTINGS_TEXT, reply_markup=settings_markup
    )
    
    return MENU_ROUTES



async def vocabulary(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Settings section where you can edit settings"""
    
    # check query type.
    await QueryType.check_query_type(update)
    
    # Define the vocabulary inline keyboard markup
    vocabulary_markup: InlineKeyboardMarkup = InlineKeyboardMarkup([   
        [
            InlineKeyboardButton("🔠 Native Language", callback_data=str(NATIVE_LANGUAGE)),
            InlineKeyboardButton("🌐 Language To Learn", callback_data=str(LANGUAGE_TO_LEARN)),
        ],
        [
            InlineKeyboardButton("<< Menu", callback_data=str(MENU)),
            InlineKeyboardButton("🎓 Knowlage Level", callback_data=str(KNOWLEDGE_LEVEL)),
        ]
    ])
    
    # Send message with text and appended InlineKeyboard
    await QueryType.reply_query(
        update=update, reply_text=WELCOME_MESSAGE_TEXT, reply_markup=vocabulary_markup
        )

    return MENU_ROUTES


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    
    # check query type.
    await QueryType.check_query_type(update=update)
    
    # Define the help inline keyboard markup
    vocabulary_markup: InlineKeyboardMarkup = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("<< Menu", callback_data=str(MENU)),
            ]
    ])

    # Send message with text and appended InlineKeyboards
    await QueryType.reply_query(
        update=update,reply_text=VOCABULARY_TEXT, reply_markup=vocabulary_markup
    )
    
    return MENU_ROUTES

async def search_word(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    
    # check query type.
    await QueryType.check_query_type(update)
    
    # Define search word inline keyboard markup
    search_word_markup: InlineKeyboardMarkup = InlineKeyboardMarkup ([
            [
                InlineKeyboardButton("<< Menu", callback_data=str(MENU)),
            ]
    ])

    # Send message with text and appended InlineKeyboards   
    await QueryType.reply_query(
        update=update,reply_text=SEARCH_WORD_TEXT, reply_markup=search_word_markup
    )
    
    return MENU_ROUTES


async def archive(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    
    # check query type.
    await QueryType.check_query_type(update=update)
    
    # Define search word inline keyboard markup
    archive_markup:InlineKeyboardMarkup = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("<< Menu", callback_data=str(MENU)),
            ]
    ])
    
    # Send message with text and appended InlineKeyboards
    await QueryType.reply_query(
        update=update,reply_text=ARCHIVE_TEXT, reply_markup=archive_markup
    )
    
    return MENU_ROUTES

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    # check query type.
    await QueryType.check_query_type(update=update)
    
    # Define search word inline keyboard markup
    quiz_markup:InlineKeyboardMarkup = InlineKeyboardMarkup(   [
            [
                InlineKeyboardButton("<< Menu", callback_data=str(MENU)),
            ]
    ])
    
    # Send message with text and appended InlineKeyboards
    await QueryType.reply_query(
        update=update, reply_text=QUIZ_TEXT, reply_markup=quiz_markup
    )
    
    return MENU_ROUTES

async def word(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        # check query type.
    word = context.args[0] if context.args else None
    print(str(word))
    if word:
        # If the word is provided, send it back to the user (you can also fetch data here)
        word_definition = await GetWordServices.get_word_definition_service(word=word)
        await update.message.reply_text(f'word_definition: {word_definition}')
    else:
        # If no word is provided
        await update.message.reply_text('Please provide a word after /word.')
    
    
    return MENU_ROUTES
    
    
    


async def native_language(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    pass

async def knowledge_level(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    pass

async def language_to_learn(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    pass

async def categories(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    pass



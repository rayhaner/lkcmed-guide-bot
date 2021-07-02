from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import os, options, effectors
import logging

TOKEN = os.environ['TOKEN']
PORT = int(os.environ.get('PORT', 8443))

# LOGGERS & ERROR HANDLING
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


# CHAT FUNCTIONS
def start(update, context):
    """Send message when /start sent"""

    keyboard = [
        [InlineKeyboardButton('Campuses & Transport', callback_data='campuses_transport')],
        [InlineKeyboardButton('Food Recommendations', callback_data='food_options')],
        [InlineKeyboardButton('Extracurriculars', callback_data='extracurriculars')],
        [InlineKeyboardButton('Studying', callback_data='studying')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text='Welcome to the LKCMedicine Survival Guide for '
                                                                    'freshies! Choose any of the options below. If '
                                                                    'you ever get stuck, type /start in the chat!',
                             reply_markup=reply_markup)


campuses_transport = options.OptionsMenu(title_text='Campuses & Transport',
                                         options_list=options.CAMPUSES_TRANSPORT).make_keyboard()
food_options = options.OptionsMenu(title_text='Food Options', options_list=options.FOOD_OPTIONS).make_keyboard()
extracurriculars = options.OptionsMenu(title_text='Extracurriculars at LKCMedicine',
                                       options_list=options.EXTRACURRICULARS).make_keyboard()
studying = options.OptionsMenu(title_text='Studying in LKCMedicine', options_list=options.STUDYING).make_keyboard()

CSB_main = options.OptionsMenu(title_text='Clinical Sciences Building (Novena)',
                               options_list=options.CSB_MAIN).make_keyboard()
EMB_main = options.OptionsMenu(title_text='Experimental Medicine Building (NTU)',
                               options_list=options.EMB_MAIN).make_keyboard()
facilities_CSB = options.OptionsMenu(title_text='CSB Facilities', options_list=options.FACILITIES_CSB).make_keyboard()

shuttle_ntu_novena = options.OptionsMenu(title_text='Shuttle Bus (NTU - Novena)', options_list=options.SHUTTLE_NTU_NOVENA).make_keyboard()

food_novena = options.OptionsMenu(title_text='Food at Novena', options_list=options.FOOD_NOVENA).make_keyboard()

food_yunnan = options.OptionsMenu(title_text='Food at Yunnan Gardens', options_list=options.FOOD_YUNNAN).make_keyboard()


def switch(arg):
    """Associating query.data to tuple of (function, name)"""

    switch_dict = {
        # Main Menu
        'start': (start, 'Main Menu'),
        'campuses_transport': (campuses_transport, 'Campuses & Transport'),
        'food_options': (food_options, 'Food Options'),
        'extracurriculars': (extracurriculars, 'Extracurriculars at LKCMedicine'),
        'studying': (studying, 'Studying in LKCMedicine'),

        # CSB
        'CSB_main': (CSB_main, 'Clinical Sciences Building (Novena)'),
        'directions_CSB_location': (effectors.directions_CSB_location, 'Directions to CSB from your location'),
        'directions_CSB_novena': (effectors.directions_CSB_novena, 'Directions to CSB from Novena MRT'),
        'facilities_CSB': (facilities_CSB, 'Facilities in CSB'),
        'CSB_l5': (effectors.CSB_l5, 'CSB Level 5'),
        'CSB_l6': (effectors.CSB_l6, 'CSB Level 6'),
        'CSB_l7': (effectors.CSB_l7, 'CSB Level 7'),
        'CSB_l8': (effectors.CSB_l8, 'CSB Level 8'),
        'CSB_l20': (effectors.CSB_l20, 'CSB Level 20'),

        # EMB
        'EMB_main': (EMB_main, 'Experimental Medicine Building (NTU)'),
        'directions_EMB_location': (effectors.directions_EMB_location, 'Directions to EMB from your location'),
        'directions_EMB_pioneer': (effectors.directions_EMB_pioneer, 'Directions to EMB from Pioneer MRT'),

        # Shuttles
        'shuttle_ntu_novena': (shuttle_ntu_novena, 'Shuttle Bus (NTU - Novena)'),
        'shuttle_hall6': (effectors.shuttle_hall6, 'Hall 6 - CSB Scheduled Shuttle Bus'),
        'shuttle_EMB': (effectors.shuttle_EMB, 'EMB - CSB Regular Shuttle Bus'),
        'shuttle_yunnan': (effectors.shuttle_yunnan, 'Shuttle Bus (Yunnan Gardens)'),

        # Food
        'food_novena': (food_novena, 'Food at Novena'),
        'supply_demand': (effectors.supply_demand, 'Supply and Demand'),
        'belle_ville': (effectors.belle_ville, 'Belle-Ville Pancake Cafe'),
        'donki': (effectors.donki, 'Don Don Donki'),
        'food_yunnan': (food_yunnan, 'Food at Yunnan Gardens'),
        'food_north_spine': (effectors.food_north_spine, 'North Spine Food Court'),
        'food_south_spine': (effectors.food_south_spine, 'South Spine Food Court'),
        'crespion_canteen': (effectors.crespion_canteen, 'CresPion Canteen'),
        'other_canteens': (effectors.other_canteens, 'Other Canteens'),
        'food_phone': (effectors.food_phone, 'On Your Phone')
    }
    return switch_dict.get(arg)


def button(update, context):
    """Parses the CallbackQuery"""
    query = update.callback_query
    query.answer()
    query.delete_message()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"You selected {switch(query.data)[1]}")

    switch(query.data)[0](update, context)


def help(update, context):
    """Send message when /help sent"""
    context.bot.send_message(chat_id=update.effective_chat.id, text='You typed help!')


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=' '.join(update.message.text).upper())


def main():
    # Create updater and dispatcher
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Add commands: /start, /help
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CallbackQueryHandler(button))
    # dispatcher.add_handler(CommandHandler('CSB', goto_CSB))

    # Add commands: when anything is typed, repeat in caps
    dispatcher.add_handler(MessageHandler(Filters.text, echo))

    # Add error handling
    dispatcher.add_error_handler(error)

    # Start the bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://lkcmed-guide-bot.herokuapp.com/' + TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()

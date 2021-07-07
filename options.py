from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

# Text - Data tuples for menu options
CAMPUSES_TRANSPORT = [
    ('Clinical Sciences Building (Novena)', 'CSB_main'),
    ('Experimental Medicine Building (NTU)', 'EMB_main'),
    ('Shuttle Bus: NTU - Novena', 'shuttle_ntu_novena'),
    ('Shuttle Bus: Around Yunnan Garden', 'shuttle_yunnan'),
    ('Go Back', 'start')
]

FOOD_OPTIONS = [
    ('Food around Novena', 'food_novena'),
    ('Food around Yunnan Gardens', 'food_yunnan'),
    ('Go Back', 'start')
]

EXTRACURRICULARS = [
    ('LKCrew', 'lkcrew'),
    ('Medlee', 'medlee'),
    ("LKC Students' Medical Society", 'medsoc'),
    ('Go Back', 'start')
]

STUDYING = [
    ('Study Spots', 'study_spots'),
    ('Study Tips', 'study_tips'),
    ('Dress Code for Lessons', 'dress_code'),
    ('Apps and Websites of LKC', 'apps_websites'),
    ('Go Back', 'start')
]

CSB_MAIN = [
    ('Directions to CSB (from your location)', 'directions_CSB_location'),
    ('Directions to CSB (from Novena MRT)', 'directions_CSB_novena'),
    ('Facilities in CSB', 'facilities_CSB'),
    ('Go Back', 'campuses_transport')
]

FACILITIES_CSB = [
    ('Level 5: Learning Studio, Seminar Room, Skills Lab', 'CSB_l5'),
    ('Level 6: Communications Suites', 'CSB_l6'),
    ('Level 7: Anatomy Learning Centre, Seminar Room', 'CSB_l7'),
    ('Level 8: House Rooms, Student Lounge, Music Room, Gym, MPH', 'CSB_l8'),
    ('Level 20: Library', 'CSB_l20'),
    ('Go Back', 'CSB_main')
]

EMB_MAIN = [
    ('Directions to EMB (from your location)', 'directions_EMB_location'),
    ('Directions to EMB (from Pioneer MRT)', 'directions_EMB_pioneer'),
    ('Go Back', 'campuses_transport')
]

SHUTTLE_NTU_NOVENA = [
    ('Hall 6 - CSB Scheduled Shuttle Buses', 'shuttle_hall6'),
    ('EMB - CSB Regular Shuttle Buses', 'shuttle_EMB'),
    ('Go Back', 'campuses_transport')
]

FOOD_NOVENA = [
    ('Supply & Demand', 'supply_demand'),
    ('Belle-Ville Pancake Cafe', 'belle_ville'),
    ('Don Don Donki', 'donki'),
    ('Go Back', 'food_options')
]

FOOD_YUNNAN = [
    ('North Spine Food Court', 'food_north_spine'),
    ('South Spine Food Court', 'food_south_spine'),
    ('CresPion Canteen', 'crespion_canteen'),
    ('Other Canteens', 'other_canteens'),
    ('On Your Phone', 'food_phone'),
    ('Go Back', 'food_options')
]

STUDY_SPOTS = [
    ('Study Spot: CSB Library', 'study_CSB_library'),
    ('Study Spot: North Spine', 'study_north_spine'),
    ('Study Spot: Hall TV Lounge', 'study_hall_tv'),
    ('Study Spot: CSB House Rooms', 'study_CSB_rooms'),
    ('Go Back', 'studying')
]

STUDY_TIPS = [
    ('Study Materials', 'study_materials'),
    ('Pen & Paper vs Digital Studying', 'pen_paper_digital'),
    ('Study Methods', 'study_methods'),
    ('Research Reports', 'research_reports'),
    ('Go Back', 'studying')
]


def back_only_keyboard(home_callback, update, context):
    keyboard = [
        [InlineKeyboardButton('Go Back to Previous', callback_data=home_callback)],
        [InlineKeyboardButton('Return to Start', callback_data='start')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='<i>Go back to previous menu or return all the way to the start?</i>',
                             reply_markup=reply_markup,
                             parse_mode=ParseMode.HTML)


class OptionsMenu:
    """Object to initialize a list of options for menu traversal"""

    def __init__(self, title_text, options_list):
        self.options_list = options_list
        self.title_text = title_text

    def make_keyboard(self):
        def func(update, context):
            keyboard = []
            for text, data in self.options_list:
                keyboard.append([InlineKeyboardButton(text, callback_data=data)])

            reply_markup = InlineKeyboardMarkup(keyboard)
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=f"What do you want to know about <b>{self.title_text}</b>?",
                                     reply_markup=reply_markup, parse_mode=ParseMode.HTML)

        return func

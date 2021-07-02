from telegram import ParseMode
import options


def directions_CSB_location(update, context):
    context.bot.send_location(chat_id=update.effective_chat.id, latitude=1.3219004809007464,
                              longitude=103.84906813460427)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='<b>How to get directions to CSB</b>\n1. Tap on the map above\n2. Select the '
                                  '"Directions" button\n3. Choose your application of choice to obtain directions!',
                             parse_mode=ParseMode.HTML)
    options.back_only_keyboard('CSB_main', update, context)


def directions_CSB_novena(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='<b>Getting to CSB from Novena MRT (~5mins walk)</b>\n1. Exit the train station via '
                                  'Exit A and walk uphill towards the direction of Tan Tock Seng Hospital (TTSH); do '
                                  'not enter TTSH! \n2. Walk straight on down the path till you come to a steep hill '
                                  'on your left hand side.\n3. Walk up the hill (crawl, roll, run, whichever method '
                                  'that yields the least suffering) and get to the top.\n4. Walk straight down the '
                                  'path ahead. Do not turn left or right! The path straight should lead you all the '
                                  'way to the National Centre for Infectious Disease (NCID) right in front of '
                                  'you.\n5. Cross the traffic light and viola, you have reached CSB!',
                             parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Please wait while we send you a video of the route...')
    context.bot.send_video(chat_id=update.effective_chat.id,
                           video=open('assets\CSB_novena_video.mp4', 'rb'),
                           caption='Video: CSB from Novena MRT',
                           width=1920, height=1080)

    options.back_only_keyboard('CSB_main', update, context)


def directions_EMB_location(update, context):
    context.bot.send_location(chat_id=update.effective_chat.id, latitude=1.344847028422491,
                              longitude=103.67860760416102)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='<b>How to get directions to EMB</b>\n1. Tap on the map above\n2. Select the '
                                  '"Directions" button\n3. Choose your application of choice to obtain directions!',
                             parse_mode=ParseMode.HTML)
    options.back_only_keyboard('EMB_main', update, context)


def directions_EMB_pioneer(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Getting to EMB from Pioneer MRT</b>\n1. From Pioneer MRT Station, exit the "
                                  "station via Exit B and proceed to the bus stop.\n2. Wait for the Campus Rider / "
                                  "Campus Green bus at the front of the bus stop to come and pick you up! (do note "
                                  "that there isn't really a good estimate for this bus, so just be early in "
                                  "case)\n3. Once on board, take the Campus Rider (Green) bus and alight at the very "
                                  "first stop in NTU (this is the Hall 1 bus stop)\n4. At the Hall 1 bus stop, "
                                  "wait for the Campus Red bus and board it to continue your journey before alighting "
                                  "at the School of Biological Sciences (SBS) bus stop and EMB will be right in front "
                                  "of you!\n\nAlternatively, you can also take Campus Rider and alight at TCT Lecture "
                                  "Theatre, then walk through School of Biological Sciences to reach EMB.",
                             parse_mode=ParseMode.HTML)

    options.back_only_keyboard('CSB_main', update, context)


# CSB FACILITIES FUNCTIONS

# TODO CHECK FOR COPYRIGHT FOR IMAGES
def CSB_l5(update, context):
    """Showcase facilities in CSB Level 5"""
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Here's what you can find at Level 5 of CSB: <b>Learning Studio</b>, <b>Seminar "
                                  "Room 5</b>, <b>Practical Skills Lab!</b>",
                             parse_mode=ParseMode.HTML)
    # context.bot.send_photo(chat_id=update.effective_chat.id,
    #                        photo=open('assets\CSB_learning_studio.jpg', 'rb'),
    #                        caption='Learning Studio, CSB Level 5')
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Level 5 is where the <b>Learning Studio</b>, <b>Seminar Room</b> and <b>Practical "
                                  "Skills Lab</b> are located. Do check out the <b>Learning Studio</b> when you get "
                                  "the chance! It's a huge space with tables to fit every team for one batch of "
                                  "students for us to conduct TBL. <b>Seminar Rooms</b> are generally used for "
                                  "lessons as well, such as Medical Humanities classes. The <b>Practical Skills "
                                  "Lab</b> is where we hone our clinical skills like suturing and wound dressing, "
                                  "and even has a Simulation Ward!",
                             parse_mode=ParseMode.HTML)
    options.back_only_keyboard('facilities_CSB', update, context)


# TODO Attach image of Comms Suites
def CSB_l6(update, context):
    """Showcase facilities in CSB Level 6"""
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Here's what you can find at Level 6 of CSB: <b>Communications Suites</b>!",
                             parse_mode=ParseMode.HTML)

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Level 6 is generally where our simulated Consultation Rooms (<b>Communications "
                                  "Suites</b>) are located. Students get to meet with Simulated Patients (SP) as part "
                                  "of the Clinical Procedures and Communications lessons and practice hands-on "
                                  "knowledge learned in theory classes! Do grab your chance to be a "
                                  "'doctor-for-a-day' when lessons are held here.",
                             parse_mode=ParseMode.HTML)
    options.back_only_keyboard('facilities_CSB', update, context)


# TODO Attach image of Anat Lab
def CSB_l7(update, context):
    """Showcase facilities in CSB Level 7"""
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Here's what you can find at Level 6 of CSB: <b>Anatomy Learning Centre</b>, "
                                  "<b>Seminar Rooms 7A & 7B</b>!",
                             parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="At Level 7, get ready to don your lab coat as you venture into human anatomy here "
                                  "at the <b>Anatomy Learning Centre</b>. Our lab is filled with plastinated models "
                                  "that aid students in their learning and visualisations of the body's anatomy so be "
                                  "sure to pay attention and learn well from these models and treat them with "
                                  "respect!",
                             parse_mode=ParseMode.HTML)
    options.back_only_keyboard('facilities_CSB', update, context)


# TODO Attach image of Gym / House Room / etc
# TODO CHECK FOR COPYRIGHT FOR IMAGES
def CSB_l8(update, context):
    """Showcase facilities in CSB Level 5"""
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Here's what you can find at Level 5 of CSB: <b>House Room</b>, <b>Student "
                                  "Lounge</b>, <b>Music Room</b>, <b>Gym</b>, <b>Multipurpose Hall</b>!",
                             parse_mode=ParseMode.HTML)
    # CHECK FOR COPYRIGHT
    # context.bot.send_photo(chat_id=update.effective_chat.id,
    #                        photo=open('assets\CSB_gym.png', 'rb'),
    #                        caption='Gym, CSB Level 8')
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Level 8 is where all the fun is at. Level 8 houses our very own <b>Gym</b>, "
                                  "so if you're feeling tired from studying and mugging head down for a short "
                                  "workout! LKC has 5 Houses and hence, there are 5 different <b>House Rooms</b> at "
                                  "fLevel 8 so feel free to hop into your own House Room to rest, chill, "
                                  "or even study. It's quite a conducive environment! Alternatively, do check out our "
                                  "<b>Student Lounge</b> as well which carry various games and a pool table, "
                                  "and seats for a place to generally chill and relax. The <b>Music Room</b> right "
                                  "next to it is also good for de-stressing, so do go in there and let your inner "
                                  "self out!",
                             parse_mode=ParseMode.HTML)
    options.back_only_keyboard('facilities_CSB', update, context)


# TODO CHECK FOR COPYRIGHT FOR IMAGES
def CSB_l20(update, context):
    """Showcase facilities in CSB Level 20"""
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Here's what you can find at Level 20 of CSB: <b>Library</b>!",
                             parse_mode=ParseMode.HTML)
    # CHECK FOR COPYRIGHT
    # context.bot.send_photo(chat_id=update.effective_chat.id,
    #                        photo=open('assets\CSB_library.jpg', 'rb'),
    #                        caption='Gym, CSB Level 8')
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Fancy to bring out the mugger in you? Have a TBL coming and need a quiet place "
                                  "besides home or hall to do your preparations? Look no further as the <b>CSB "
                                  "Library</b> is open for students to study daily till 9pm! Besides its really "
                                  "conducive and quiet atmosphere, the library houses a printing station for you to "
                                  "print any necessary materials if required, and is really spacious and clean! Being "
                                  "on the 20th floor, the library boasts a really splendid scenic 360 degrees view of "
                                  "the Singapore skyline as it's a good view to look at while relaxing your eyes "
                                  "after hours of studying. Be sure to bring a jacket though, the weather in the "
                                  "library can be really chilly!",
                             parse_mode=ParseMode.HTML)
    options.back_only_keyboard('facilities_CSB', update, context)


# SHUTTLE BUS FUNCTIONS

def shuttle_hall6(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>HALL 6 - CSB (SCHEDULED) SHUTTLE BUS</b>\nWhenever the M1 or M2 students have "
                                  "lessons at CSB, a shuttle bus will be scheduled, which departs from Hall 6 (which "
                                  "is right next to Crescent and Pioneer Halls) to CSB. This shuttle bus is scheduled "
                                  "to leave 1 hour before the stipulated start time of your lesson at CSB, "
                                  "so don't be late! This shuttle bus departs ON TIME so don't be late! (the bus "
                                  "really doesn't wait for people so be there or be square!) After your lesson, "
                                  "a shuttle bus will also be scheduled which travels from CSB back to Hall 6, "
                                  "and this bus leaves 30 minutes after the stipulated time at which the lesson ends. "
                                  "So if you plan to stick around CSB to chill in the house rooms or study in the "
                                  "library, then you will most likely end up missing this scheduled bus, "
                                  "but don't worry, there's still the option of the regular buses!",
                             parse_mode=ParseMode.HTML)
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open('assets\hall6_bus_sample.png', 'rb'),
                           caption='This is a sample timetable for the scheduled shuttle bus. This can be found on '
                                   'your iLKC portal and is updated monthly. The number on the left signifies the '
                                   'year that it is catered for (e.g. 1 = M1 students), and on the right is the '
                                   'estimated no. of pax (though the buses are large so there is some leeway about '
                                   'the maximum pax).')
    options.back_only_keyboard('shuttle_ntu_novena', update, context)


def shuttle_EMB(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>EMB - CSB (REGULAR) SHUTTLE BUS</b>\nOn Mondays to Fridays (except Public "
                                  "holidays), every hour starting from 8.15am, a shuttle bus runs from NTU "
                                  "Experimental Medicine Building (EMB) to NTU Novena Clinical Sciences Building ("
                                  "CSB), and from CSB back to EMB. It's a 2-way system running concurrently and buses "
                                  "leave both EMB and CSB at the same time!\n\nThe shuttle bus starts at 8.15am at "
                                  "both EMB and CSB, and continues every hour, at 9.15am, 10.15am, 11.15am, 1.15pm, "
                                  "2.15pm, 3.15pm, 4.15pm and 5.30pm. Take note there's no 12.15pm bus as our bus "
                                  "uncles have to grab their lunch too! And as for the 5.30pm bus it is the last "
                                  "shuttle bus of the day and there isn't a 5.15pm bus for some reasons unknown to "
                                  "man.\n\nDo note that this bus leaves from / travels to EMB, not Hall 6 - so if "
                                  "you're living in hall at Crespion, you'll have to travel to / from EMB if you want "
                                  "to take this bus to get to CSB. Also, the regular shuttle bus also stops by some "
                                  "other bus stops around NTU, so do consider boarding / alighting the bus from these "
                                  "stops instead if they are more convenient depending on where you are in NTU!",
                             parse_mode=ParseMode.HTML)
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open('assets\emb_bus_sample.jpg', 'rb'),
                           caption='This is the route taken for the EMB - CSB shuttle; note that it does not stop at '
                                   'Hall 6 or CresPion!')
    options.back_only_keyboard('shuttle_ntu_novena', update, context)


def shuttle_yunnan(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>NTU Yunnan Garden Shuttle Buses</b>\nThere are various shuttle bus services "
                                  "which are available within the NTU Yunnan Garden Campus which are utilised by "
                                  "students from all the faculties in NTU, but for LKC students, these three bus "
                                  "services are the ones that are most useful and relevant to us! Do download the NTU "
                                  "U-Wave App and the NTU GO! App as well to read in details about the exact stops "
                                  "for each bus route. (Available for both Android and iOS users)",
                             parse_mode=ParseMode.HTML)
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open('assets\CLR_route.jpg', 'rb'),
                           caption='<b>Campus Loop Red</b>\nThis bus goes around the campus in a CLOCKWISE direction, '
                                   'and stops at Hall 1 (which is across the road from Crespion)',
                           parse_mode=ParseMode.HTML)
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open('assets\CLB_route.jpg', 'rb'),
                           caption='<b>Campus Loop Blue</b>\nThis bus goes around the campus in an ANTI-CLOCKWISE '
                                   'direction, and stops at Hall 6 (which is adjacent to Crespion)',
                           parse_mode=ParseMode.HTML)
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open('assets\CR_route.jpg', 'rb'),
                           caption='<b>Campus Rider Green</b>\nThis bus stops at Hall 1 (which is across the road '
                                   'from Crespion), and shuttles between Pioneer MRT Station and the NTU Yunnan '
                                   'Garden Campus so have no worries coming to school by MRT!',
                           parse_mode=ParseMode.HTML)
    options.back_only_keyboard('campuses_transport', update, context)


# FOOD FUNCTIONS

def supply_demand(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Supply and Demand</b>\nThe price is worth it and the food is really another "
                                  "class. There’s a wide variety of pastas, rice bowls and even pizzas too! Oh and "
                                  "yes, they have fantastic sides such as cheese fries! Highly recommended would be "
                                  "the vegetarian pizza (yes it is good seriously), truffle mushroom chicken pizza, "
                                  "carbonara and their herb infused chicken! Do take note there’s a student/staff "
                                  "menu, and also the normal public menu. But fret not, ordering from the public menu "
                                  "will allow you to receive a 20% student discount so you won’t have to worry too "
                                  "much about the price!",
                             parse_mode=ParseMode.HTML)
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open('assets\supply_demand.jpg', 'rb'),
                           caption='Source: https://burpple-2.imgix.net/venue_images/lkc_091117-3-jpg_4051_original')
    options.back_only_keyboard('food_novena', update, context)


def belle_ville(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Belle-Ville Pancake Cafe</b>\nFor pancake fans who can eat pancakes at any time "
                                  "of the day, this is for you! With tall, jiggly, fluffy, stacked pancakes, "
                                  "be sure to indulge in this savoury! It’s more of a dessert place to be honest but "
                                  "oh wells, you make the rule on what you wanna eat for lunch!",
                             parse_mode=ParseMode.HTML)
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open('assets\pancake.jpg', 'rb'),
                           caption='Source: https://www.misstamchiak.com/wp-content/uploads/2019/04/Belle'
                                   '-villepancakecafefeaturedimage1.jpg')
    options.back_only_keyboard('food_novena', update, context)


def donki(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Don Don Donki</b>\nDon Don Donki has awesome Japanese food! From fried chicken "
                                  "karaage to savoury mentai salmon sushi, be sure to check out Don Don Donki's wide "
                                  "selection of Japanese food. Perfect for a day when you wish for a proper yet "
                                  "simple and delicious meal! There’s even an area for you to sit down and eat your "
                                  "meals so don’t worry about having to stand awkwardly around to finish your meals.",
                             parse_mode=ParseMode.HTML)
    options.back_only_keyboard('food_novena', update, context)


def food_north_spine(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>North Spine: Honey Chicken Chop Rice (Taiwan Ichiban)</b>\nThe meat is super "
                                  "juicy and tender, and it’s a really huge portion because it’s like the XL Taiwan "
                                  "chicken you get at a Shilin Night Market! The amount of powder on the chicken was "
                                  "balanced and not overbearing. Do check out their forms of chicken too! Each one is "
                                  "equally good.",
                             parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>North Spine: Halal Food (Indonesian BBQ)</b>\nFor our Muslim friends out there "
                                  "have no worry! The store here has a really good variety of nice Halal food such as "
                                  "Nasi Lemak, Lontong and even has Indonesian BBQ dishes which look mouth-watering "
                                  "and really attractive. Do check them out too!",
                             parse_mode=ParseMode.HTML)
    options.back_only_keyboard('food_yunnan', update, context)


def food_south_spine(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>South Spine: Xiao Long Bao</b>\nThe Xiao Long Bao here is quite legit, the meat "
                                  "and broth in the bao is fragrant and tasty! If you’re craving for some authentic "
                                  "Chinese cuisine here’s a place you could head down to check out.",
                             parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>South Spine: Carbonara (Pasta Express)</b>\nReally rich and creamy! The "
                                  "toppings are solid too, with plenty of meat as well as an oozing soft boil egg "
                                  "with runny egg yolk! The store also has many other pastas, and you’re even able to "
                                  "have the liberty to mix and match so you won’t get bored of what you’re eating.",
                             parse_mode=ParseMode.HTML)
    options.back_only_keyboard('food_yunnan', update, context)


def crespion_canteen(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>CresPion: Mookata (Thai Food Stall)</b>\nFor a 5 person mookata, it’s so worth "
                                  "it as there's a really big portion and the price is so affordable! There’s no need "
                                  "to run out of NTU to find mookata when you have one good one right here in NTU. "
                                  "They do serve other dishes too besides mookata, such as basil chicken, salted egg "
                                  "chicken, tomyum soup… Try them all!",
                             parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>CresPion: Vegetarian Salad (Healthy Salad)</b>\nFret not to all our vegetarians "
                                  "out there!! There’s also vegetarian options available for you too! Healthy Salad "
                                  "provides a wide variety of topping for salad and it’s really delicious! They have "
                                  "a wide range from simple vegetables to even Tamago eggs! And for our "
                                  "non-vegetarian friends, fret not too for they offer non-vegetarian toppings too "
                                  "such as black pepper chicken or smoked duck which are really nice too.",
                             parse_mode=ParseMode.HTML)
    options.back_only_keyboard('food_yunnan', update, context)


def other_canteens(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Canteen 2: Salted Egg Yolk Chicken Rice (Mini Wok)</b>\nThe salted egg is the "
                                  "signature dish of the store and it’s honestly really one of the best! It’s savoury "
                                  "yet not overly salty and the chicken goes so well with plain rice. The portion of "
                                  "meat is really generous too!",
                             parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Canteen 9: Gong Bao Rice (Jiulixiang Sichuan Cuisine)</b>\nSpicy food lovers "
                                  "out there, this is something you should try before graduation!!",
                             parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Canteen 16: Curry Pork Tonkatsu + Hanjuku Eggs (Japanese Food)</b>\nThe curry "
                                  "here is pretty legit and savoury and not very spicy! The thickness of the curry is "
                                  "just right too, and the portion of the meat covers half the plate too (WOW). It’s "
                                  "quite a good deal so do try it out!",
                             parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>North Hill Food Court: Fish and Chips (Uncle Anderson Western Food "
                                  "Stall)</b>\nReally good western food, with really good fish and a really crispy "
                                  "batter! It isn’t too floury like some places and the meat is thick yet tender. "
                                  "They even come with a side of fries and mashed potato with black pepper gravy "
                                  "which goes so well together!",
                             parse_mode=ParseMode.HTML)
    options.back_only_keyboard('food_yunnan', update, context)


def food_phone(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Telegram Groups</b>\nJoin the <b>Raydy's Beehoon</b> Telegram group here at "
                                  "https://t.me/raydyntu and start ordering your supper! It delivers right to your "
                                  "hall’s bus stop or admin office so you don’t even have to walk far for supper! "
                                  "Pre-orders are available, as well as ordering straight from the food truck by just "
                                  "going down to the food truck when it arrives at your hall and buying on the spot. "
                                  "Supper life has never been simpler than this!\n\nThere are other supper groups "
                                  "too, such as <b>Ah Lian Bee Hoon Delivery</b> (it’s an open group so there’s no "
                                  "invite link for that), but do feel free to ask your friendly seniors about it! "
                                  "They will be able to add you into the group, as we’re all fighting for the common "
                                  "cause of a hearty supper.",
                             parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Cates App (iOS / Android)</b>\nThis app allows you to order food from the food "
                                  "stalls/restaurants around NTU campus and have it delivered to a common collection "
                                  "point at Crespion Hall (next to the hall office) - so if you don't want to eat "
                                  "from the Crespion canteen but don't want to travel to the other canteens, "
                                  "consider this option!",
                             parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Instagram Food Reviews</b>\nAnd for those who may be interested to follow Food "
                                  "Reviews done by students all over NTU, do follow the few Instagram pages "
                                  "below!\n\n@ntufoodies -> https://instagram.com/ntufoodies?igshid=1gooxk3wb1zu0\n\n"
                                  "@ntufoodlist -> https://instagram.com/ntufoodlist?igshid=1vugd4yvvisgd",
                             parse_mode=ParseMode.HTML)
    options.back_only_keyboard('food_yunnan', update, context)

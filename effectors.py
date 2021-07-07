from telegram import ParseMode
import options, os

dirname = os.path.dirname(__file__)


def directions_CSB_location(update, context):
    context.bot.send_location(chat_id=update.effective_chat.id, latitude=1.3219004809007464,
                              longitude=103.84906813460427)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='<b>How to get directions to CSB (on mobile)</b>\n1. Tap on the map above\n2. '
                                  'Select the "Directions" button\n3. Choose your application of choice to obtain '
                                  'directions!',
                             parse_mode=ParseMode.HTML)
    options.back_only_keyboard('CSB_main', update, context)


def directions_CSB_novena(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='<b>Getting to CSB from Novena MRT (~5mins walk)</b>\n\n1. Exit the train station via'
                                  ' Exit A and walk uphill towards the direction of Tan Tock Seng Hospital (TTSH); do '
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
                           video=open(os.path.join(dirname, 'assets', 'CSB_novena_video.mp4'), 'rb'),
                           caption='Video: CSB from Novena MRT',
                           width=1920, height=1080)

    options.back_only_keyboard('CSB_main', update, context)


def directions_EMB_location(update, context):
    context.bot.send_location(chat_id=update.effective_chat.id, latitude=1.344847028422491,
                              longitude=103.67860760416102)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='<b>How to get directions to EMB (on mobile)</b>\n\n1. Tap on the map above\n2. '
                                  'Select the "Directions" button\n3. Choose your application of choice to obtain '
                                  'directions!',
                             parse_mode=ParseMode.HTML)
    options.back_only_keyboard('EMB_main', update, context)


def directions_EMB_pioneer(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Getting to EMB from Pioneer MRT</b>\n\n1. From Pioneer MRT Station, exit the "
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


def CSB_l8(update, context):
    """Showcase facilities in CSB Level 5"""
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Here's what you can find at Level 5 of CSB: <b>House Room</b>, <b>Student "
                                  "Lounge</b>, <b>Music Room</b>, <b>Gym</b>, <b>Multipurpose Hall</b>!",
                             parse_mode=ParseMode.HTML)

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


def CSB_l20(update, context):
    """Showcase facilities in CSB Level 20"""
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Here's what you can find at Level 20 of CSB: <b>Library</b>!",
                             parse_mode=ParseMode.HTML)

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
                             text="<b>HALL 6 - CSB (SCHEDULED) SHUTTLE BUS</b>\n\nWhenever the M1 or M2 students have "
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
                           photo=open(os.path.join(dirname, 'assets', 'hall6_bus_sample.png'), 'rb'),
                           caption='This is a sample timetable for the scheduled shuttle bus. This can be found on '
                                   'your iLKC portal and is updated monthly. The number on the left signifies the '
                                   'year that it is catered for (e.g. 1 = M1 students), and on the right is the '
                                   'estimated no. of pax (though the buses are large so there is some leeway about '
                                   'the maximum pax).')
    options.back_only_keyboard('shuttle_ntu_novena', update, context)


def shuttle_EMB(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>EMB - CSB (REGULAR) SHUTTLE BUS</b>\n\nOn Mondays to Fridays (except Public "
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
                           photo=open(os.path.join(dirname, 'assets', 'emb_bus_sample.jpg'), 'rb'),
                           caption='This is the route taken for the EMB - CSB shuttle; note that it does not stop at '
                                   'Hall 6 or CresPion!')
    options.back_only_keyboard('shuttle_ntu_novena', update, context)


def shuttle_yunnan(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>NTU Yunnan Garden Shuttle Buses</b>\n\nThere are various shuttle bus services "
                                  "which are available within the NTU Yunnan Garden Campus which are utilised by "
                                  "students from all the faculties in NTU, but for LKC students, these three bus "
                                  "services are the ones that are most useful and relevant to us! Do download the NTU "
                                  "U-Wave App and the NTU GO! App as well to read in details about the exact stops "
                                  "for each bus route. (Available for both Android and iOS users)",
                             parse_mode=ParseMode.HTML)
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open(os.path.join(dirname, 'assets', 'CLR_route.jpg'), 'rb'),
                           caption='<b>Campus Loop Red</b>\n\nThis bus goes around the campus in a CLOCKWISE direction,'
                                   ' and stops at Hall 1 (which is across the road from Crespion)',
                           parse_mode=ParseMode.HTML)
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open(os.path.join(dirname, 'assets', 'CLB_route.jpg'), 'rb'),
                           caption='<b>Campus Loop Blue</b>\n\nThis bus goes around the campus in an ANTI-CLOCKWISE '
                                   'direction, and stops at Hall 6 (which is adjacent to Crespion)',
                           parse_mode=ParseMode.HTML)
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open(os.path.join(dirname, 'assets', 'CR_route.jpg'), 'rb'),
                           caption='<b>Campus Rider Green</b>\n\nThis bus stops at Hall 1 (which is across the road '
                                   'from Crespion), and shuttles between Pioneer MRT Station and the NTU Yunnan '
                                   'Garden Campus so have no worries coming to school by MRT!',
                           parse_mode=ParseMode.HTML)
    options.back_only_keyboard('campuses_transport', update, context)


# FOOD FUNCTIONS

def supply_demand(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Supply and Demand</b>\n\nThe price is worth it and the food is really another "
                                  "class. There’s a wide variety of pastas, rice bowls and even pizzas too! Oh and "
                                  "yes, they have fantastic sides such as cheese fries! Highly recommended would be "
                                  "the vegetarian pizza (yes it is good seriously), truffle mushroom chicken pizza, "
                                  "carbonara and their herb infused chicken! Do take note there’s a student/staff "
                                  "menu, and also the normal public menu. But fret not, ordering from the public menu "
                                  "will allow you to receive a 20% student discount so you won’t have to worry too "
                                  "much about the price!",
                             parse_mode=ParseMode.HTML)
    # context.bot.send_photo(chat_id=update.effective_chat.id,
    #                        photo=open(os.path.join(dir, 'assets', 'supply_demand.jpg'), 'rb'),
    #                        caption='Source: https://burpple-2.imgix.net/venue_images/lkc_091117-3-jpg_4051_original')
    options.back_only_keyboard('food_novena', update, context)


def belle_ville(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Belle-Ville Pancake Cafe</b>\n\nFor pancake fans who can eat pancakes at any time"
                                  " of the day, this is for you! With tall, jiggly, fluffy, stacked pancakes, "
                                  "be sure to indulge in this savoury! It’s more of a dessert place to be honest but "
                                  "oh wells, you make the rule on what you wanna eat for lunch!",
                             parse_mode=ParseMode.HTML)
    # context.bot.send_photo(chat_id=update.effective_chat.id,
    #                        photo=open(os.path.join(dir, 'assets', 'pancake.jpg'), 'rb'),
    #                        caption='Source: https://www.misstamchiak.com/wp-content/uploads/2019/04/Belle'
    #                                '-villepancakecafefeaturedimage1.jpg')
    options.back_only_keyboard('food_novena', update, context)


def donki(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Don Don Donki</b>\n\nDon Don Donki has awesome Japanese food! From fried chicken "
                                  "karaage to savoury mentai salmon sushi, be sure to check out Don Don Donki's wide "
                                  "selection of Japanese food. Perfect for a day when you wish for a proper yet "
                                  "simple and delicious meal! There’s even an area for you to sit down and eat your "
                                  "meals so don’t worry about having to stand awkwardly around to finish your meals.",
                             parse_mode=ParseMode.HTML)
    options.back_only_keyboard('food_novena', update, context)


def food_north_spine(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>North Spine: Honey Chicken Chop Rice (Taiwan Ichiban)</b>\n\nThe meat is super "
                                  "juicy and tender, and it’s a really huge portion because it’s like the XL Taiwan "
                                  "chicken you get at a Shilin Night Market! The amount of powder on the chicken was "
                                  "balanced and not overbearing. Do check out their forms of chicken too! Each one is "
                                  "equally good.",
                             parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>North Spine: Halal Food (Indonesian BBQ)</b>\n\nFor our Muslim friends out there "
                                  "have no worry! The store here has a really good variety of nice Halal food such as "
                                  "Nasi Lemak, Lontong and even has Indonesian BBQ dishes which look mouth-watering "
                                  "and really attractive. Do check them out too!",
                             parse_mode=ParseMode.HTML)
    options.back_only_keyboard('food_yunnan', update, context)


def food_south_spine(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>South Spine: Xiao Long Bao</b>\n\nThe Xiao Long Bao here is quite legit, the meat"
                                  " and broth in the bao is fragrant and tasty! If you’re craving for some authentic "
                                  "Chinese cuisine here’s a place you could head down to check out.",
                             parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>South Spine: Carbonara (Pasta Express)</b>\n\nReally rich and creamy! The "
                                  "toppings are solid too, with plenty of meat as well as an oozing soft boil egg "
                                  "with runny egg yolk! The store also has many other pastas, and you’re even able to "
                                  "have the liberty to mix and match so you won’t get bored of what you’re eating.",
                             parse_mode=ParseMode.HTML)
    options.back_only_keyboard('food_yunnan', update, context)


def crespion_canteen(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>CresPion: Mookata (Thai Food Stall)</b>\n\nFor a 5 person mookata, it’s so worth "
                                  "it as there's a really big portion and the price is so affordable! There’s no need "
                                  "to run out of NTU to find mookata when you have one good one right here in NTU. "
                                  "They do serve other dishes too besides mookata, such as basil chicken, salted egg "
                                  "chicken, tomyum soup… Try them all!",
                             parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>CresPion: Vegetarian Salad (Healthy Salad)</b>\n\nFret not to all our vegetarians"
                                  " out there!! There’s also vegetarian options available for you too! Healthy Salad "
                                  "provides a wide variety of topping for salad and it’s really delicious! They have "
                                  "a wide range from simple vegetables to even Tamago eggs! And for our "
                                  "non-vegetarian friends, fret not too for they offer non-vegetarian toppings too "
                                  "such as black pepper chicken or smoked duck which are really nice too.",
                             parse_mode=ParseMode.HTML)
    options.back_only_keyboard('food_yunnan', update, context)


def other_canteens(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Canteen 2: Salted Egg Yolk Chicken Rice (Mini Wok)</b>\n\nThe salted egg is the "
                                  "signature dish of the store and it’s honestly really one of the best! It’s savoury "
                                  "yet not overly salty and the chicken goes so well with plain rice. The portion of "
                                  "meat is really generous too!",
                             parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Canteen 9: Gong Bao Rice (Jiulixiang Sichuan Cuisine)</b>\n\nSpicy food lovers "
                                  "out there, this is something you should try before graduation!!",
                             parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Canteen 16: Curry Pork Tonkatsu + Hanjuku Eggs (Japanese Food)</b>\n\nThe curry "
                                  "here is pretty legit and savoury and not very spicy! The thickness of the curry is "
                                  "just right too, and the portion of the meat covers half the plate too (WOW). It’s "
                                  "quite a good deal so do try it out!",
                             parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>North Hill Food Court: Fish and Chips (Uncle Anderson Western Food "
                                  "Stall)</b>\n\nReally good western food, with really good fish and a really crispy "
                                  "batter! It isn’t too floury like some places and the meat is thick yet tender. "
                                  "They even come with a side of fries and mashed potato with black pepper gravy "
                                  "which goes so well together!",
                             parse_mode=ParseMode.HTML)
    options.back_only_keyboard('food_yunnan', update, context)


def food_phone(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Telegram Groups</b>\n\nJoin the <b>Raydy's Beehoon</b> Telegram group here at "
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
                             text="<b>Cates App (iOS / Android)</b>\n\nThis app allows you to order food from the food "
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


# EXTRACURRICULARS FUNCTIONS

def lkcrew(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>LKCrew</b>\n\n<b>LKCrew</b> is a student interest group established in 2019 with "
                                  "the aim of creating a welcoming and nurturing environment for dancers of all "
                                  "levels in LKC. Through regular dance classes, sharings and performance "
                                  "opportunities, we hope to share the joys of dancing with every student, "
                                  "and foster a sense of community through a shared passion for dance!\n\nWhether you "
                                  "have 10 years of experience or none at all, LKCrew is the place for you! all "
                                  "members have the chance to learn various genres from contemporary to hip hop, "
                                  "opportunities to share and choreograph and perform together at school events like "
                                  "PBnJ! The best part? There are no expectations on commitment, sharings are held "
                                  "every 2-3 weeks, but you can join us whenever you can! Follow us on instagram "
                                  "@lkc.rew or join our tele chat!!",
                             parse_mode=ParseMode.HTML)
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open(os.path.join(dirname, 'assets', 'lkcrew.png'), 'rb'))
    options.back_only_keyboard('extracurriculars', update, context)


def medlee(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Medlee</b>\n\nLove to sing in the shower? Well, so do we! <b>Medlee</b> is a stud"
                                  "ent-led acapella group formed in early 2016 by a couple of students from LKCMedicine"
                                  " who are passionate about making music and having fun. This CCA has been passed down"
                                  " since then. Today, we have nine M1s and ten M2s who are currently active members. "
                                  "Our talented seniors also often come down for teaching sessions even though they "
                                  "have stepped down. In Medlee, we help each other grow musically, produce acappella "
                                  "covers and arrange our own music. Most importantly, we savour the experience of "
                                  "singing with friends that share the same passion for good music as us. Come join "
                                  "us if you want to:\n- improve your singing skills\n- learn how to sing in a "
                                  "group\n- learn beatboxing\n- hone your music theory knowledge\n- try to arrange a "
                                  "song\n- have tons of fun with music-loving friends!\n\nDon’t worry if you have no "
                                  "formal singing experience - as long as you’re passionate about singing, "
                                  "just give it a shot and sign up!",
                             parse_mode=ParseMode.HTML)
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open(os.path.join(dirname, 'assets', 'medlee.jpg'), 'rb'))
    options.back_only_keyboard('extracurriculars', update, context)


def medsoc(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>LKC Students' Medical Society</b>\n\n<i>What does LKCMedSoc do?</i>\n\nThe LKC "
                                  "Students’ Medical Society (LKCMedSoc) is a student-led organisation in its 8th "
                                  "iteration, consisting of all students studying in LKC. Our overarching goals are "
                                  "two-fold: to enhance the university experience of all LKCMedicine students, "
                                  "and to represent the interests and needs of LKCMedicine students to LKCMedicine "
                                  "and NTU.",
                             parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<i>Who is part of LKCMedSoc?</i>\n\nLKCMedSoc consists of several committees: the "
                                  "Executive Committee (ExCo), Academic, Careers, Research, Welfare, "
                                  "Year Representatives, House Representatives, Sports, Arts and Culture, "
                                  "Freshmen Orientation Programme, Dinner and Dance, Publicity and Publications, "
                                  "International Relations, Overseas Community Involvement Projects (OCIP) and Local "
                                  "Community Involvement Projects (LCIP).",
                             parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<i>What does the ExCo do?</i>\n\nThe ExCo comprises a total of 7 members: the "
                                  "President, Vice-President (Education), Vice-President (Wellbeing), "
                                  "Honorary General Secretary, Treasurer, Programmes Director and Outreach "
                                  "Director.\n\nApart from working hand in hand with the various committees on the "
                                  "organisation of events and activities, the Executive Committee participates in "
                                  "regular dialogue with the LKCMedicine faculty to represent the views and concerns "
                                  "of the student body.",
                             parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<i>MedSoc Website</i> (www.lkcmedsoc.com)\n\nThe one-stop portal for all the "
                                  "information pertaining to LKC Student Body. The website provides an overview of "
                                  "the events occurring throughout the year. Information regarding student activity "
                                  "groups such as OCIPs, LCIPs and SIGs are collated and updated here. Post-event "
                                  "photos taken by the P&P Committee are posted on the website too!\n\n<b>Event "
                                  "Registration</b>: LKC has many events occurring throughout the year organised "
                                  "internally by LKC or externally by organisations, such as the healthcare clusters. "
                                  "The event registration page allows an overview of numerous upcoming activities "
                                  "with their description and sign-up links.\n\n<b>Room Booking</b>: Need a room for "
                                  "meeting? Need a room for studying? Need a room for events? The room booking form "
                                  "provides a hassle-free experience for booking of the rooms in CSB.\n\n<b>Ideas / "
                                  "Feedback Platform</b>: If you have an exciting idea, you can propose it on the "
                                  "feedback platform on the website. The new ideas will be placed up for voting by "
                                  "the LKC student body. If it is well-received, LKC ExCo will provide you with "
                                  "support for further discussion with the faculty. Similarly, if you have any "
                                  "feedback, it can be posted through this platform. To provide an overview of all "
                                  "the amazing ideas and constructive feedback, a writeup for the rejected, "
                                  "ongoing and approved items are updated on this platform.",
                             parse_mode=ParseMode.HTML)
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open(os.path.join(dirname, 'assets', 'medsoc.png'), 'rb'))
    options.back_only_keyboard('extracurriculars', update, context)


# STUDYING FUNCTIONS

def study_CSB_library(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Clinical Sciences Building Library</b>\n\nThe CSB library has individual "
                                  "cubicles or open tables for you to choose from. It also has a pantry where you can "
                                  "study while eating, or even gather with your friends for an intense game of "
                                  "Avalon!! Located on the 20th storey, the CSB library has an extremely gorgeous "
                                  "scenery!\n\nOpening hours:\n(Phase 2) Mon - Fri: 8.00am - 9.30pm\nSat & Sun: "
                                  "8.00am - 6.30pm\nPH: Closed\n\n<u>Ratings</u>\nAvailability of seats: "
                                  "4/5\nCharging ports: 4/5\nFree WiFi: 5/5\nAircon: 5/5\n<b>Overall Rating</b>: 4.5/5",
                             parse_mode=ParseMode.HTML)
    options.back_only_keyboard('study_spots', update, context)

def study_north_spine(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>North Spine / Lee Wee Nam Library</b>\n\nNorth Spine is where all the hustle "
                                  "and bustle is, with a supermarket, bubble tea and a food court. There are seats "
                                  "and tables near the lecture theatres where you can study while eating. It is also "
                                  "amazing that in the heart of a bustling North Spine is NTU’S flagship library: Lee "
                                  "Wee Nam Library, which is super conducive and quiet for studying.\n\nOpening "
                                  "hours (Lee Wee Nam Library):\nMon - Fri 8.30am - 9.30pm\nSat 8.30am - "
                                  "5.00pm\n\n<u>Ratings</u>\nAvailability of seats: 2/5\nCharging ports: 2/5\nFree "
                                  "WiFi: 5/5\nAircon: 2.5/5 (There is aircon in LWN library, but no aircon at North "
                                  "Spine outside of the library)\n<b>Overall Rating</b>: 3/5",
                             parse_mode=ParseMode.HTML)
    options.back_only_keyboard('study_spots', update, context)


def study_hall_tv(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Hall TV Lounge</b>\n\nWith a TV and (free) aircon, the hall TV lounge is the "
                                  "perfect place to gather with your friends to play and chill! It is also easily "
                                  "accessible for those staying in the hall, with one in each block. When you are "
                                  "tired of studying in your own hall room, the hall TV lounge would be a great "
                                  "alternative study place (if you manage to chope it)! However, it's often "
                                  "preoccupied with hall residents who go there to play games (mahjong) and chill "
                                  "with friends (especially at night! It may be more available during the day) so "
                                  "your mileage may vary with regard to availability of the lounge.\n\nOpening hours: "
                                  "24/7\n\n<u>Ratings</u>\nAvailability of seats: 2/5\nCharging ports: 5/5\nFree "
                                  "WiFi: 5/5\nAircon: 5/5\n<b>Overall Rating</b>: 5/5",
                             parse_mode=ParseMode.HTML)
    options.back_only_keyboard('study_spots', update, context)


def study_CSB_rooms(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>CSB House Rooms / TV Lounge</b>\n\nIf you don’t like dead silence but still "
                                  "want a conducive environment, then house rooms are the perfect study spots for "
                                  "you! With the occasional hustle and bustle from your house mates chilling and "
                                  "playing, you can take a break anytime to exercise at the gym or to play pool or "
                                  "foosball at the Student Lounge!\n\nOpening hours: Same as CSB opening "
                                  "hours\n\n<u>Ratings</u>\nAvailability of seats: 3/5\nCharging ports: 4/5\nFree "
                                  "WiFi: 5/5\nAircon: 5/5\n<b>Overall Rating</b>: 3.5/5",
                             parse_mode=ParseMode.HTML)
    options.back_only_keyboard('study_spots', update, context)


def study_materials(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Study Materials</b>\n\nThe main source of information should be school notes "
                                  "and lecture slides which are designed according to our curriculum’s learning "
                                  "objectives. However, you may also opt to use additional textbooks to supplement "
                                  "school notes. A complete list of the recommended textbooks are available in the "
                                  "iLKC portal >> Phase 1 >> Y1 Recommended Textbooks List.\n\nSeveral sections of "
                                  "these textbooks may be labelled as “additional reading material” by the school. "
                                  "Despite being labelled as additional material, these are compulsory as material "
                                  "from these sections are examinable.",
                             parse_mode=ParseMode.HTML)
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open(os.path.join(dirname, 'assets', 'textbooks.png'), 'rb'),
                           caption="Textbooks that are more commonly used by seniors")
    options.back_only_keyboard('study_tips', update, context)


def pen_paper_digital(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Pen & Paper vs Digital</b>\n\nComing from a pre-tertiary education background, "
                                  "many of you are likely to be accustomed to the traditional pen & paper method for "
                                  "note-taking and studying. However, given the huge amount of content to be covered "
                                  "in medical school, students are encouraged to turn to digital note-taking and "
                                  "study methods. All LKC students will be provided with an iPad Mini 5, "
                                  "hence purchasing an Apple Pen is highly recommended to allow for flexible "
                                  "note-taking directly on the device. Having digital notes also comes with the "
                                  "convenience of having your notes with you at all times!\n\nHowever, do not feel "
                                  "pressured if you wish to continue using a pen & paper study method, as there are "
                                  "seniors who do so based on personal preference. Ultimately, every decision you "
                                  "make about how you choose to study should be comfortable to you rather than "
                                  "others.\n\nShould you choose to use digital study methods, additional applications "
                                  "are highly recommended for your iPad. <i><b>Notability</b></i> ($12.98) offers "
                                  "great compatibility between iPads and Macbooks as notes are synced on both "
                                  "devices. <i><b>GoodNotes 5</b></i> ($10.98) has the premier in-built file "
                                  "organisation, <i><b>Microsoft OneNote</b></i> (free!) features pages with infinite "
                                  "boundaries for those who enjoy mind maps and diagrams. Feel free to explore these "
                                  "applications to find one that suits you. While the default notes application of "
                                  "iOS can also be used, it is discouraged due to lack of additional functionality "
                                  "and poor organisation capacity. Do not be dissuaded by the price tags as these "
                                  "applications are an investment for your next five years!",
                             parse_mode=ParseMode.HTML)
    options.back_only_keyboard('study_tips', update, context)


def study_methods(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Study Methods</b>\n\nTime management is crucial as you traverse your way "
                                  "through medical school. It is of paramount importance that you find a study method "
                                  "that suits your learning style, while simultaneously giving high yield for time "
                                  "invested. As a general guideline, the school blocks out three hours of protected "
                                  "study time for each TBL session. However, be prepared to spend double that time to "
                                  "properly internalise and memorise the content, depending on the complexity of that "
                                  "particular topic. <i><b>VLC Media Player</b></i> is a highly recommended tool as "
                                  "it allows you to speed up lecture recordings by up to 2x to save time. Without "
                                  "this, the combined duration of lecture recordings could vary from between three to "
                                  "six hours, excluding the time taken to commit the content to memory.",
                             parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Given the amount of content there is to understand and memorise, it is important "
                                  "to keep in mind the differences between low-yield passive studying (e.g. listening "
                                  "to lecture recordings) and high-yield active recall. How much you learn is not "
                                  "dependent on how long you spend, but rather how efficient your use of time is. The "
                                  "most common methods of studying are creating personal notes and "
                                  "<i><b>Anki</b></i>, to be covered below.",
                             parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Seniors often create their own digital notes (e.g. on a word document) after "
                                  "reviewing the lecture recordings and slides so that they are able to review the "
                                  "content more easily in the future. Notes can be organised based on the learning "
                                  "outcomes that are provided by the school. It is also important to be able to draw "
                                  "links between the content that you have learnt in the past as the various systems "
                                  "in the human body are highly interconnected with one another. Drawing these links "
                                  "enhances your understanding of the subject, in turn improving your ability to "
                                  "recall concepts with ease.",
                             parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<i><b>Anki</b></i> ($34.98 on iOS, free on Android) is a study tool that relies on "
                                  "flashcards as your primary form of memorising content. This study method is a "
                                  "systematic and automated system that employs the concepts of active recall and "
                                  "spaced repetition to aid in the formation of long-term memory. While it is a "
                                  "common and useful study method, DO NOT fall into the Anki hype train without "
                                  "taking into consideration your style of learning. There are plenty of people who "
                                  "do not rely on Anki but do well, and Anki does not guarantee good results even "
                                  "when used correctly. While Anki is most useful at allowing your mind to form "
                                  "relationships between two or more concepts (e.g. cause-and-effect relationships) "
                                  "but will not help you understand content if you have conceptual misunderstandings. "
                                  "Seniors will conduct a talk on how to Anki effectively in the near future if you "
                                  "are interested, so do look out for that!",
                             parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Ultimately, what you choose to do boils down to personal preference. Give yourself "
                                  "time to explore what works for you. Your year 1 formative exam is a good gauge on "
                                  "whether your style is a good fit for you.",
                             parse_mode=ParseMode.HTML)
    options.back_only_keyboard('study_tips', update, context)


def research_reports(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Research Reports</b>\n\nYou are expected to write about four science practical "
                                  "reports alongside reflective writing pieces every year. Being a formal report, "
                                  "all claims made in your report must be backed with citations from peer-reviewed "
                                  "journals and other reliable sources. <i><b>Google Scholar</b></i> is a helpful "
                                  "tool for you to quickly find and cite relevant papers for your report with ease. "
                                  "The <i><b>NTU LibGenie</b></i> extension allow you to access journal articles that "
                                  "have a paywall, through the NTU Library.",
                             parse_mode=ParseMode.HTML)
    options.back_only_keyboard('study_tips', update, context)


def dress_code(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Dress Code</b>\n\nBroadly speaking, there are three types of dress codes that "
                                  "you will wear to different lessons:\n\n1. <u>Formal Wear</u>\nMales: Pretty standard"
                                  "ised! A formal shirt (with sleeves rolled up above the elbow), long pants, dress "
                                  "shoes. A tie is usually not necessary unless otherwise stated.\nFemales: Pretty "
                                  "versatile! Typical outfits include dress/jumpsuit/formal blouse with skirt/long "
                                  "office pants, court shoes/heels/flats. Nail varnish is highly discouraged!\n\n2. "
                                  "<u>Informal Wear</u>\nMales & Females: anything casual you want (so long it is "
                                  "appropriate!), so that includes shirts, shorts, skirts, etc.\n\n3. <u>Semi-formal "
                                  "Wear</u>\nMales and Females: T-shirt, long pants, covered shoes (no slippers)",
                             parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Dress codes differ based on what type of lesson you are attending:\n\n1. "
                                  "<u>Foundations of Clinical Practice (FCP)</u>\nWhen the lesson involves "
                                  "interacting with Simulated Patients (SPs) or even real patients, <b>Formal Wear "
                                  "with White Coat</b> is mandatory.\nWhen no SPs or patients are involved, "
                                  "<b>Semi-formal Wear</b> is allowed.\n\n2. <u>Science Practicals / Anatomy "
                                  "Practicals</u>\nFor most science and anatomy lab sessions, <b>Semi-formal Wear "
                                  "with Lab Coat</b> should be worn.\nSome science practical sessions will have SPs, "
                                  "in which case <b>Formal Wear with White Coat</b> is mandatory.\n\n3. <u>Team Based "
                                  "Learning (TBL) sessions</u>\n<b>Informal Wear</b> is acceptable for TBLs.",
                             parse_mode=ParseMode.HTML)
    options.back_only_keyboard('studying', update, context)


def apps_websites(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>iLKC</b> (Website) & <b>iStudent</b> (iPad "
                                  "App)\n<i>https://ilkc.ntu.edu.sg/</i>\n\nThe bread and butter website for lessons "
                                  "at LKC, iLKC is where you can obtain most resources pertaining to school. Most "
                                  "importantly, here you can access your school timetable and any TBL preparatory "
                                  "materials (e.g. videos and slides). Feedback submission, examination results, "
                                  "shuttle bus schedule and a variety of other information is available here. "
                                  "iStudent is the iPad app equivalent for iLKC.",
                             parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>iFolio</b> (Website & iPad App)\n<i>https://ifolio.ntu.edu.sg/</i>\n\niFolio is "
                                  "a portal where you can submit some types of assignments, usually Science Practical "
                                  "reports and FCP Clinical Methods checklists. Faculty are able to provide feedback "
                                  "on your work via this portal as well. Hence, it is important to bring your iPad "
                                  "along to FCP Clinical Methods sessions so that your tutors will be able to input "
                                  "their feedback into your iFolio account.",
                             parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>NTULearn</b> (Website)\n<i>https://ntulearn.ntu.edu.sg/</i>\n\nNTULearn is a "
                                  "portal used in your FCP Clinical Procedures / Clinical Communications and Medical "
                                  "Humanities lessons. For those classes, this is where lesson materials are "
                                  "disseminated. Assignment submissions for those classes (e.g. reflective writing "
                                  "essays) are done through NTULearn as well.",
                             parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>LKCPortal SMOTS</b> (Website)\n<i>https://lkcportal.ntu.edu.sg/</i>\n\nSMOTS is "
                                  "a website where you will be able to access and download video recordings of your "
                                  "FCP Clinical Communications sessions. You can use this as a way to review your "
                                  "communication and history taking skills to improve in subsequent sessions! Note "
                                  "that the SMOTS website is only available if you are on the NTU WiFi, therefore it "
                                  "is not accessible from home.",
                             parse_mode=ParseMode.HTML)
    options.back_only_keyboard('studying', update, context)
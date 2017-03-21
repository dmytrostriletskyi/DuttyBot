from rutetider import Timetable, UserPosition, Subscribers, CurrentDates
from additional_data import token, database_url
from display_schedule import display_schedule
from reply_keyboard_markups import Keyboard
import message_handler_groups
from flask import Flask, request
import datetime
import telebot
import os

server = Flask(__name__)

bot = telebot.TeleBot(token)
keyboard = Keyboard(bot)


@bot.message_handler(commands=['start'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Получить расписание')
    user_markup.row('Получить расписание по подписке')
    user_markup.row('Время пар')
    user_markup.row('Обновления', 'Обратная связь')
    bot.send_message(message.from_user.id, 'Выберите пункт меню:', reply_markup=user_markup)


@bot.message_handler(func=lambda mess: "Главное меню" == mess.text, content_types=['text'])
def handle_text(message):
    keyboard.main_menu(message)


@bot.message_handler(func=lambda mess: "Время пар" == mess.text, content_types=['text'])
def handle_text(message):
    bot.send_sticker(message.chat.id, 'BQADAgADOwADTnfcEXgpqbcHcL3wAg')


@bot.message_handler(func=lambda mess: "Обновления" == mess.text, content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, 'Обновления и дополнительную информацию можно посмотреть тут — \
                     https://telegram.me/dutbotupdates')


@bot.message_handler(func=lambda mess: "Обратная связь" == mess.text, content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, 'По вопросам и предложениям:\n • @dmytryistriletskyi\n • \
                     dmytryi.striletskyi@gmail.com')


@bot.message_handler(func=lambda mess: 'Получить расписание' == mess.text, content_types=['text'])
def handle_text(message):
    UserPosition(database_url).set_getting_position(str(message.chat.id))
    keyboard.get_all_faculties(message)


@bot.message_handler(func=lambda mess: 'Інформаційних технологій' == mess.text or
                     'Телекомунікацій' == mess.text or 'Інформаційної безпеки' == mess.text or
                     'Загальні підрозділи' == mess.text or 'Заочне навчання' == mess.text or
                     'Менеджменту та підприємництва' == mess.text, content_types=['text'])
def handle_text(message):
    UserPosition(database_url).set_faculty_position(str(message.chat.id), message.text)

    if message.text != "Загальні підрозділи" and message.text != 'Заочне навчання':
        keyboard.stable_six_courses(message)

    if message.text == "Загальні підрозділи":
        keyboard.stable_one_course(message)

    if message.text == "Заочне навчання":
        keyboard.stable_three_courses(message)


@bot.message_handler(func=lambda mess: '1 курс' == mess.text or '2 курс' == mess.text or
                     '3 курс' == mess.text or '4 курс' == mess.text or '5 курс' == mess.text or
                     '6 курс' == mess.text or '7 курс' == mess.text, content_types=['text'])
def handle_text(message):
    UserPosition(database_url).set_course_position(str(message.chat.id), message.text[:1])
    faculty, course = UserPosition(database_url).get_faculty_and_group(str(message.chat.id))
    groups_list = Timetable(database_url).get_all_groups(faculty, course)
    groups_list.sort()
    keyboard.group_list_by_faculty_and_group(groups_list, message)


message_handler_groups.message_handler_groups(bot, UserPosition(database_url), keyboard)


@bot.message_handler(func=lambda mess: 'На сегодня' == mess.text or 'На завтра' == mess.text or
                     'Подписаться на эту группу' == mess.text or 'Главное меню' == mess.text,
                     content_types=['text'])
def handle_text(message):
    today, tomorrow = CurrentDates(database_url).get_dates()
    group = UserPosition(database_url).verification(str(message.chat.id))
    weekday_index = datetime.datetime.strptime(today, '%d.%m.%Y').date().weekday()

    if message.text == 'На сегодня':
        lessons = Timetable(database_url).get_lessons(group, today)
        lessons = [lessons[key] for key in sorted(lessons.keys())]

        if weekday_index == 5:
            bot.send_message(message.chat.id, 'Выходной день')
        elif weekday_index == 6:
            bot.send_message(message.chat.id, 'Выходной день')
        else:
            bot.send_message(message.chat.id, 'Расписание на сегодня ({0}):'.format(today[:5]))
            bot.send_message(message.chat.id, display_schedule(lessons))

    if message.text == 'На завтра':
        lessons = Timetable(database_url).get_lessons(group, tomorrow)
        lessons = [lessons[key] for key in sorted(lessons.keys())]

        if weekday_index == 4:
            bot.send_message(message.chat.id, 'Выходной день')
        elif weekday_index == 5:
            bot.send_message(message.chat.id, 'Выходной день')
        else:
            bot.send_message(message.chat.id, 'Расписание на завтра ({0}):'.format(tomorrow[:5]))
            bot.send_message(message.chat.id, display_schedule(lessons))

    if message.text == 'Подписаться на эту группу':
        Subscribers(database_url).create_subscribers()
        Subscribers(database_url).add_subscriber(str(message.chat.id), group)
        bot.send_message(message.chat.id, 'Вы подписались на группу {0}.'.format(group))


@bot.message_handler(func=lambda mess: "Получить расписание по подписке" == mess.text, content_types=['text'])
def handle_text(message):
    CurrentDates(database_url).add_dates('26.03.2017', '27.03.2017')
    group = Subscribers(database_url).get_subscriber_group(str(message.chat.id))
    today, tomorrow = CurrentDates(database_url).get_dates()
    weekday_index = datetime.datetime.strptime(today, '%d.%m.%Y').date().weekday()

    lessons = Timetable(database_url).get_lessons(group, today)
    lessons_today = [lessons[key] for key in sorted(lessons.keys())]

    lessons = Timetable(database_url).get_lessons(group, tomorrow)
    lessons_tomorrow = [lessons[key] for key in sorted(lessons.keys())]

    if weekday_index == 4:
        bot.send_message(message.chat.id, 'Расписание на сегодня ({0}):'.format(today[:5]))
        bot.send_message(message.chat.id, display_schedule(lessons_today))
        bot.send_message(message.chat.id, 'Расписание на завтра ({0}):'.format(tomorrow[:5]))
        bot.send_message(message.chat.id, 'Выходной день.')
    elif weekday_index == 5:
        bot.send_message(message.chat.id, 'Выходные дни.')
    elif weekday_index == 6:
        bot.send_message(message.chat.id, 'Расписание на сегодня ({0}):'.format(today[:5]))
        bot.send_message(message.chat.id, 'Выходной день.')
        bot.send_message(message.chat.id, 'Расписание на завтра ({0}):'.format(tomorrow[:5]))
        bot.send_message(message.chat.id, display_schedule(lessons_tomorrow))
    else:
        bot.send_message(message.chat.id, 'Расписание на сегодня ({0}):'.format(today[:5]))
        bot.send_message(message.chat.id, display_schedule(lessons_today))
        bot.send_message(message.chat.id, 'Расписание на завтра ({0}):'.format(tomorrow[:5]))
        bot.send_message(message.chat.id, display_schedule(lessons_tomorrow))


@bot.message_handler(func=lambda mess: 'Вернуться назад' == mess.text, content_types=['text'])
def handle_text(message):
    user_position = UserPosition(database_url).back_keyboard(str(message.chat.id))
    if user_position == 1:
        UserPosition(database_url).cancel_getting_started(str(message.chat.id))
        keyboard.main_menu(message)

    if user_position == 2:
        UserPosition(database_url).cancel_faculty(str(message.chat.id))
        keyboard.get_all_faculties(message)

    if user_position == 3:
        UserPosition(database_url).cancel_course(str(message.chat.id))
        faculty = UserPosition(database_url).verification(str(message.chat.id))
        if faculty != "Загальні підрозділи" and faculty != 'Заочне навчання':
            keyboard.stable_six_courses(message)

        if faculty == "Загальні підрозділи":
            keyboard.stable_one_course(message)

        if faculty == "Заочне навчання":
            keyboard.stable_three_courses(message)

    if user_position == 4:
        UserPosition(database_url).cancel_group(str(message.chat.id))
        faculty, course = UserPosition(database_url).get_faculty_and_group(str(message.chat.id))
        groups_list = Timetable(database_url).get_all_groups(faculty, course)
        groups_list.sort()
        keyboard.group_list_by_faculty_and_group(groups_list, message)


@server.route('/' + token, methods=['POST'])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "POST", 200


@server.route("/")
def web_hook():
    bot.remove_webhook()
    bot.set_webhook(url='https://glacial-lowlands-23073.herokuapp.com/' + token)
    return "CONNECTED", 200

server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))

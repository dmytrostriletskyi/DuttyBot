from flask import Flask, request
import telebot



import sys
import os

import basicMarkupRows
import controllers.printController as printController
import dataBaseSelections 
import dataLib 
import config
import dateOperations as schedule

import dj_database_url
import psycopg2


import middlewareUserData
import basicMarkupRows
import backButton

import botMessageHandlerSubscribe

bot = telebot.TeleBot(config.TOKEN)

middleware = middlewareUserData.middlewareUserData()
basicMarkupRows = basicMarkupRows.basicMarkupRows(bot)
backButton = backButton.backButton()
selectData = dataBaseSelections.dataBaseSelections()

server = Flask(__name__)



@bot.message_handler(commands=['start'])
def handle_text(message):
	user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
	user_markup.row("Получить расписание")
	user_markup.row("Время пар") 
	user_markup.row('Обновления', 'Обратная связь')
	bot.send_message(message.from_user.id, 'Выберите пункт меню:', reply_markup=user_markup)


@bot.message_handler(func=lambda mess: "Вернуться в главное меню" == mess.text, content_types=['text'])
def handle_text(message):

	basicMarkupRows.getBackIntoMainMenu(message)


@bot.message_handler(func=lambda mess: "Время пар" == mess.text, content_types=['text'])
def handle_text(message):	

	middleware.otherFeature(message.chat.first_name, message.chat.last_name, message.chat.id, 'sticker', message.chat.username)
	bot.send_sticker(message.chat.id, 'BQADAgADOwADTnfcEXgpqbcHcL3wAg')


@bot.message_handler(func=lambda mess: "Обновления" == mess.text, content_types=['text'])
def handle_text(message):

    middleware.otherFeature(message.chat.first_name, message.chat.last_name, message.chat.id, 'news', message.chat.username)
    bot.send_message(message.chat.id, 'Обновления и дополнительную информацию можно посмотреть тут — https://telegram.me/dutbotupdates')


@bot.message_handler(func=lambda mess: "Обратная связь" == mess.text, content_types=['text'])
def handle_text(message):

    middleware.otherFeature(message.chat.first_name, message.chat.last_name, message.chat.id, 'feedback', message.chat.username)
    bot.send_message(message.chat.id, 'По вопросам и предложениям:\n • @dmytryistriletskyi\n • dmytryi.striletskyi@gmail.com')


@bot.message_handler(func=lambda mess: "Получить расписание" == mess.text, content_types=['text'])
def handle_text(message):

	basicMarkupRows.markRowGetFacultyList(message)

	middleware.getUser(message.chat.first_name, message.chat.last_name, message.chat.id, message.chat.username)
	print ('Insert user`s data:', message.chat.first_name, message.chat.last_name, message.chat.id, message.chat.username)



botMessageHandlerSubscribe.botMessageHandlerSubscribe(bot, middleware, selectData, printController)



@bot.message_handler(func=lambda mess: 'Інформаційних технологій' == mess.text or \
											'Телекомунікацій' == mess.text or \
											'Інформаційної безпеки' == mess.text or \
											'Загальні підрозділи' == mess.text or \
											'Заочне навчання' == mess.text or \
											'Менеджменту та підприємництва' == mess.text, content_types=['text'])
def getSelectedFaculty(message):

	middleware.updateFaculty(message.text, str(message.chat.id))

	if message.text != "Загальні підрозділи" and message.text != 'Заочне навчання':
		basicMarkupRows.markRowMajorCourseList(message)
		print ('Update chatid and faculty:', message.text, message.chat.id)

	if message.text == "Загальні підрозділи":
		basicMarkupRows.markRowOverallCourseList(message)
		print ('Update chatid and faculty:', message.text, message.chat.id)
		
	if message.text == "Заочне навчання":
		basicMarkupRows.markRowDistanceCourseList(message)
		
		print ('Update chatid and faculty:', message.text, message.chat.id)


@bot.message_handler(func=lambda mess: '1 курс' == mess.text or \
											'2 курс' == mess.text or \
											'3 курс' == mess.text or \
											'4 курс' == mess.text or \
											'5 курс' == mess.text or \
											'6 курс' == mess.text or \
											'7 курс' == mess.text, content_types=['text'])
def getSelectedCourse(message):

	middleware.updateCourse(message.text[:1], str(message.chat.id))
	print ('Update course: ', message.chat.id, message.text[:1])

	fucAndCourse = middleware.getFacultyAndGroup(str(message.chat.id))
	print ('Take faculty and course to db-select: ', fucAndCourse[0], fucAndCourse[1])

	groupList = selectData.selectGroup(fucAndCourse[0], fucAndCourse[1])
	print ('Exit grouplist:', groupList)

	basicMarkupRows.markRowGroupList(groupList, message)



# @bot.message_handler(func=lambda mess: '-' in mess.text, content_types=['text'])
@bot.message_handler(func=lambda mess: mess.text[-1] == '1' or \
										mess.text[-1] == '2' or \
										mess.text[-1] == '3' or \
										mess.text[-1] == '4' or \
										mess.text[-1] == '5' or \
										mess.text[-1] == '6' or \
										mess.text[-1] == '7' or \
										mess.text[-1] == 'З', content_types=['text'])
def getSelectedGroup(message):

	print ('MES TEXT: ', message.text)
	print ('MES TEXT[-1]: ', message.text[-1])
	middleware.updateGroup(message.text, str(message.chat.id))
	print ('Update group: ', message.chat.id, message.text)

	basicMarkupRows.markRowChooseDate(message)

	

# day[1] - today, day[2] - tomorrow, day[3] - week day`s index
day = selectData.selectDates()
@bot.message_handler(func=lambda mess: "На сегодня ({0})".format(day[1]) == mess.text or \
										"На завтра ({0})".format(day[2]) == mess.text or \
										"Вернуться в главное меню" == mess.text or \
										"Время пар" == mess.text or \
										"Обновления" == mess.text or \
										"Подписаться на эту группу" in mess.text or \
										"Обратная связь" == mess.text, content_types=['text'])
def lastMenu(message):
	lastGroup = middleware.summaryVerification(str(message.chat.id))
	print ('Selected group:', lastGroup)


	bot.send_message(message.chat.id, 'Убедительная просьба, по причине надвигающейся проверки, увеличить посещаемость до 15.11.2016 включительно. Спасибо!\n')


	if message.text == "На сегодня ({0})".format(day[1]):
		middleware.updateChoice('schedule', str(message.chat.id))

		if day[3] == 5:
			bot.send_message(message.chat.id, 'Расписание обновляется и недоступно до воскресенья!')

		if day[3] == 6:
			bot.send_message(message.chat.id, 'Расписание доступно только на завтрашний день!')
		
		else:
			message.text = printController.show(lastGroup, day[1])
			bot.send_message(message.chat.id, message.text)


	if message.text == "На завтра ({0})".format(day[2]):
		middleware.updateChoice('schedule', str(message.chat.id))

		if day[3] == 4:
			bot.send_message(message.chat.id, 'Получить расписание можно с воскресенья!')

		if day[3] == 5:
			bot.send_message(message.chat.id, 'Расписание обновляется и недоступно до воскресенья!')

		message.text = printController.show(lastGroup, day[2])
		bot.send_message(message.chat.id, message.text)

	if message.text == "Подписаться на эту группу":
		middleware.otherFeature(message.chat.first_name, message.chat.last_name, message.chat.id, 'subscribe', message.chat.username)
		middlewareUserData.subscribe(message.chat.first_name, message.chat.last_name, message.chat.id, lastGroup, message.chat.username)

		message.text = 'Вы подписались на группу {0}.'.format(lastGroup)
		bot.send_message(message.chat.id, message.text)

@bot.message_handler(func=lambda mess: "Вернуться назад" == mess.text, content_types=['text'])
def handle_text(message):

	emptyCount = selectData.selectBackButton(str(message.chat.id))
	print (emptyCount)


	if emptyCount == 4:
		backButton.cancelOperation(str(message.chat.id), 4)
		basicMarkupRows.getBackIntoMainMenu(message)


	if emptyCount == 3:
		backButton.cancelOperation(str(message.chat.id), 3)
		basicMarkupRows.markRowGetFacultyList(message)
		

	if emptyCount == 2:
		backButton.cancelOperation(str(message.chat.id), 2)

		faculty = backButton.facultyVerification(str(message.chat.id))

		print ('BB:', faculty)
		if faculty == 'Загальні підрозділи':
			basicMarkupRows.markRowOverallCourseList(message)

		elif faculty == 'Заочне навчання':
			basicMarkupRows.markRowDistanceCourseList(message)
			
		else:
			basicMarkupRows.markRowMajorCourseList(message)


	if emptyCount == 1:
		backButton.cancelOperation(str(message.chat.id), 1)

		fucAndCourse = middleware.getFacultyAndGroup(str(message.chat.id))
		print ('1: ', fucAndCourse[0], fucAndCourse[1])

		groupList = selectData.selectGroup(fucAndCourse[0], fucAndCourse[1])
		print ('2:', groupList)

		basicMarkupRows.markRowGroupList(groupList, message)


	if emptyCount == 0:
		backButton.cancelOperation(str(message.chat.id), 0)

		fucAndCourse = middleware.getFacultyAndGroup(str(message.chat.id))
		print ('11: ', fucAndCourse[0], fucAndCourse[1])

		groupList = selectData.selectGroup(fucAndCourse[0], fucAndCourse[1])
		print ('22:', groupList)

		basicMarkupRows.markRowGroupList(groupList, message)



@server.route('/' + config.TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "POST", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=config.DOMAIN + config.TOKEN)
    return "CONNECTED", 200

server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
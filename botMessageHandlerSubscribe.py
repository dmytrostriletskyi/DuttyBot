def botMessageHandlerSubscribe(bot, middlewareUserData, selectData, printController):
	@bot.message_handler(func=lambda mess: "Получить расписание по подписке" == mess.text, content_types=['text'])
	def handle_text(message):
		subscribedGroup = selectData.selectSubscribe(str(message.chat.id))
		print ('APP:', subscribedGroup)


		day = selectData.selectDates()
		print ('BOT MESS HANDLER:', day)
		if day[3] == '4':
			bot.send_message(message.chat.id, 'Расписание на сегодня ({0}):'.format(day[1]))
			message.text = printController.show(subscribedGroup, day[1])
			bot.send_message(message.chat.id, message.text)

			bot.send_message(message.chat.id, 'Расписание на завтра ({0}):'.format(day[2]))
			bot.send_message(message.chat.id, 'Выходной день.')

		if day[3] == '5':
			bot.send_message(message.chat.id, 'Выходные дни')


		if day[3] == '6':
			bot.send_message(message.chat.id, 'Расписание на сегодня ({0}):'.format(day[1]))
			bot.send_message(message.chat.id, 'Выходной день.')

			print (day[3])
			print (day[2])
			print (subscribedGroup)
			bot.send_message(message.chat.id, 'Расписание на завтра ({0}):'.format(day[2]))
			message.text = printController.show(subscribedGroup, day[2])
			print (str(message.text))
			bot.send_message(message.chat.id, message.text)



		if subscribedGroup == 'Вы не подписаны ни на одну группу.':
			message.text = 'Вы не подписаны ни на одну группу.\nЧтобы подписаться, вам необходимо выбрать факультет, курс и группу, а после нажать на соответствующую кнопку.'
			bot.send_message(message.chat.id, message.text)
			bot.send_message(message.chat.id, 'https://telegram.me/dutbotupdates')
		else:
			middlewareUserData.otherFeature(message.chat.first_name, message.chat.last_name, message.chat.id, 'subscribe', message.chat.username)
			bot.send_message(message.chat.id, 'Вы подписаны на группу {0}.'.format(subscribedGroup))
			bot.send_message(message.chat.id, 'Расписание на сегодня ({0}):'.format(day[1]))
			message.text = printController.show(subscribedGroup, day[1])
			bot.send_message(message.chat.id, message.text)

			bot.send_message(message.chat.id, 'Расписание на завтра ({0}):'.format(day[2]))
			message.text = printController.show(subscribedGroup, day[2])
			bot.send_message(message.chat.id, message.text)

import telebot
import dataLib
import dataBaseSelections 

selectData = dataBaseSelections.dataBaseSelections()
day = selectData.selectDates()

class basicMarkupRows():
	def __init__(self, bot):
		super(basicMarkupRows, self).__init__()

		self.bot = bot

	def getBackIntoMainMenu(self, message):
		self.message = message

		user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
		user_markup.row("Получить расписание")
		user_markup.row("Получить расписание по подписке")
		user_markup.row("Время пар")
		user_markup.row('Обновления', 'Обратная связь')
		self.bot.send_message(message.from_user.id, 'Выберите пункт меню:', reply_markup=user_markup)
		
		
	def markRowGroupList(self, groupList, message):
		self.groupList = groupList
		self.message = message

		length = len(self.groupList)

		edge = (length + 1) // 2
		length -= 1

		group_markup = telebot.types.ReplyKeyboardMarkup(True, False)
		group_markup.row('Вернуться назад')
		for i in range(0, edge):
			if groupList[i] == groupList[length-i]:
				group_markup.row(groupList[i])
				break
			group_markup.row(groupList[i], groupList[length-i])
		self.bot.send_message(self.message.from_user.id, 'Выберите группу:', reply_markup=group_markup)


	def markRowGetFacultyList(self, message):
		self.message = message

		faculty_markup = telebot.types.ReplyKeyboardMarkup(True, False)
		faculty_markup.row('Вернуться назад')
		for faculty in dataLib.facultyList:
			faculty_markup.row(faculty)
		self.bot.send_message(self.message.from_user.id, 'Выберите факультет:', reply_markup=faculty_markup)


	def markRowChooseDate(self, message):
		self.message = message

		date_markup = telebot.types.ReplyKeyboardMarkup(True, False)
		date_markup.row("На сегодня ({0})".format(day[1]), "На завтра ({0})".format(day[2]))
		date_markup.row('Время пар', 'Вернуться назад')
		date_markup.row('Подписаться на эту группу')
		date_markup.row('Вернуться в главное меню')
		date_markup.row('Обратная связь', 'Обновления')

		self.bot.send_message(self.message.from_user.id, 'Выберите дату:', reply_markup=date_markup)


	def markRowMajorCourseList(self, message):
		self.message = message

		course_markup = telebot.types.ReplyKeyboardMarkup(True, False)
		course_markup.row('Вернуться назад')
		course_markup.row('1 курс', '4 курс')
		course_markup.row('2 курс', '5 курс')
		course_markup.row('3 курс', '6 курс')
		self.bot.send_message(self.message.from_user.id, 'Выберите курс:', reply_markup=course_markup)


	def markRowDistanceCourseList(self, message):
		self.message = message

		course_markup = telebot.types.ReplyKeyboardMarkup(True, False)
		course_markup.row('Вернуться назад')
		course_markup.row('3 курс')
		course_markup.row('6 курс')
		course_markup.row('7 курс')
		self.bot.send_message(self.message.from_user.id, 'Выберите курс:', reply_markup=course_markup)


	def markRowOverallCourseList(self, message):
		self.message = message

		course_markup = telebot.types.ReplyKeyboardMarkup(True, False)
		course_markup.row('Вернуться назад')
		course_markup.row('1 курс')
		self.bot.send_message(self.message.from_user.id, 'Выберите курс:', reply_markup=course_markup)
	


import dj_database_url
import psycopg2

import config 

class dataBaseSelections():
	def __init__(self):
		super(dataBaseSelections, self).__init__()

		db_info = dj_database_url.config(default=config.DBSRC)
		self.connection = psycopg2.connect(database=db_info.get('NAME'),
		    								user=db_info.get('USER'),
		    								password=db_info.get('PASSWORD'),
		    								host=db_info.get('HOST'),
		    								port=db_info.get('PORT'))

		self.cursor = self.connection.cursor()


	def selectGroup(self, faculty, course):
		self.faculty = faculty
		self.course = course
		groupList = []
	
		self.cursor.execute("SELECT groupa FROM tt713 WHERE faculty = %s AND course = %s", (self.faculty, self.course))
		
		for group in self.cursor:
		    groupList.append(group[0])

		groupList = list(set(groupList))
		
		return groupList


	def selectSchedule(self, group, date):
		self.group = group
		self.date = date

		self.cursor.execute("SELECT schedule FROM tt713 WHERE groupa = %s AND dateFirst = %s", (self.group, self.date))

		schedule = self.cursor.fetchone()[0]
		return schedule


	def selectBackButton(self, chatid):
		self.chatid = chatid
		emptyList = []

		self.cursor.execute("SELECT * FROM statistic WHERE id IN (SELECT max(id) FROM statistic WHERE chatid = (%s) AND choice != (%s) AND choice != (%s) AND choice != (%s))", (self.chatid, 'news', 'sticker', 'feedback'))
		
		for i, e in enumerate(self.cursor.fetchone()):
			if e == 'empty':
				emptyList.append(e)

		return len(emptyList)


	def selectDates(self):
		self.cursor.execute("SELECT * FROM dateapp")
		
		dates = []
		for day in self.cursor.fetchone():
			dates.append(day)

		return dates

	def selectSubscribe(self, chatid):
		self.chatid = chatid

		self.cursor.execute("SELECT * FROM subscribers WHERE id IN (SELECT max(id) FROM subscribers WHERE chatid = (%s))", (self.chatid, ))


		try:
			subscribedGroup = self.cursor.fetchone()[4]
		except TypeError:
			subscribedGroup = "Вы не подписаны ни на одну группу."

		print ('selectSubscribe:', subscribedGroup)
		print ('selectSubscribe:', type(subscribedGroup))

		
		return subscribedGroup
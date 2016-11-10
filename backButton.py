import dj_database_url
import psycopg2


import config 


class backButton():

	def __init__(self):
		super(backButton, self).__init__()

		db_info = dj_database_url.config(default=config.DBSRC)
		self.connection = psycopg2.connect(database=db_info.get('NAME'),
		    								user=db_info.get('USER'),
		    								password=db_info.get('PASSWORD'),
		    								host=db_info.get('HOST'),
		    								port=db_info.get('PORT'))

		self.cursor = self.connection.cursor()

	def cancelFaculty(self, chatid):
		self.chatid = chatid

		self.cursor.execute("UPDATE statistic SET faculty = (%s) WHERE id IN (SELECT max(id) FROM statistic WHERE chatid = (%s))", ('empty', self.chatid))
		self.connection.commit()


	def cancelCourse(self, chatid):
		self.chatid = chatid

		self.cursor.execute("UPDATE statistic SET course = (%s) WHERE id IN (SELECT max(id) FROM statistic WHERE chatid = (%s) AND faculty != (%s))", ('empty', self.chatid, 'empty'))
		self.connection.commit()


	def cancelGroup(self, chatid):
		self.chatid = chatid

		self.cursor.execute("UPDATE statistic SET groupa = (%s) WHERE id IN (SELECT max(id) FROM statistic WHERE chatid = (%s) AND faculty != (%s))", ('empty', self.chatid, 'empty'))
		self.connection.commit()


	def cancelWithChoice(self, chatid):
		self.chatid = chatid

		self.cursor.execute("SELECT * FROM statistic WHERE id IN (SELECT max(id) FROM statistic WHERE chatid = (%s) AND groupa != (%s) AND choice != (%s) )", (self.chatid, 'empty', 'empty'))

		userDataList = []
		for i, e in enumerate(self.cursor.fetchone()):
			if i == 6 or i == 8:
				e = 'empty'
			userDataList.append(e)

		self.cursor.execute("INSERT INTO statistic (firstname, lastname, chatid, faculty, course, groupa, choice, username) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (userDataList[1], userDataList[2], userDataList[3], userDataList[4], userDataList[5], 'empty', 'empty', userDataList[9]))
		self.connection.commit()


	def cancelOperation(self, chatid, emptyCount):

		self.chatid = chatid

		self.emptyCount = emptyCount

		if self.emptyCount == 3:
			self.cancelFaculty(self.chatid)

		if self.emptyCount == 2:
			self.cancelCourse(self.chatid)

		if self.emptyCount == 1:
			self.cancelGroup(self.chatid)

		if self.emptyCount == 0:
			self.cancelWithChoice(self.chatid)


	def facultyVerification(self, chatid):
		self.chatid = chatid

		self.cursor.execute("SELECT * FROM statistic WHERE id IN (SELECT max(id) FROM statistic WHERE chatid = (%s) AND faculty != (%s))", (self.chatid, 'empty', ))

		for i, faculty in enumerate(self.cursor.fetchone()):
			if i == 4:
				return faculty






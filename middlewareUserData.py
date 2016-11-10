import dj_database_url
import psycopg2

import config 

class middlewareUserData():
	def __init__(self):
		super(middlewareUserData, self).__init__()

		db_info = dj_database_url.config(default=config.DBSRC)
		self.connection = psycopg2.connect(database=db_info.get('NAME'),
		    								user=db_info.get('USER'),
		    								password=db_info.get('PASSWORD'),
		    								host=db_info.get('HOST'),
		    								port=db_info.get('PORT'))

		self.cursor = self.connection.cursor()


	def createStatistic(self):
		self.cursor.execute("DROP TABLE IF EXISTS statistic") 
		self.cursor.execute("CREATE TABLE IF NOT EXISTS statistic (id serial PRIMARY KEY, firstname text, lastname text, chatid text, faculty text, course text, groupa text, datepost timestamp not null default now() + '2 hours'::interval, choice text, username text);")
		self.connection.commit()


	def getUser(self, firstname, lastname, chatid, username):
		self.firstname = firstname
		self.lastname = lastname
		self.chatid = chatid
		self.username = username

		self.cursor.execute("INSERT INTO statistic (firstname, lastname, faculty, chatid, course, groupa, choice, username) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (self.firstname, self.lastname, 'empty', self.chatid, 'empty', 'empty', 'empty', self.username))
		self.connection.commit()


	def updateFaculty(self, faculty, chatid):
		self.faculty = faculty
		self.chatid = chatid

		self.cursor.execute("UPDATE statistic SET faculty = (%s) WHERE id IN (SELECT max(id) FROM statistic WHERE chatid = (%s)) AND course = (%s) AND groupa = (%s)", (self.faculty, self.chatid, 'empty', 'empty'))
		self.connection.commit()


	def updateCourse(self, course, chatid):
		self.course = course
		self.chatid = chatid

		self.cursor.execute("UPDATE statistic SET course = (%s) WHERE id IN (SELECT max(id) FROM statistic WHERE chatid = (%s)) AND groupa = (%s)", (self.course, self.chatid, 'empty'))
		self.connection.commit()


	def updateGroup(self, group, chatid):
		self.groupa = group
		self.chatid = chatid
		self.cursor.execute("UPDATE statistic SET groupa = (%s) WHERE id IN (SELECT max(id) FROM statistic WHERE chatid = (%s)) AND groupa = (%s)", (self.groupa, self.chatid, 'empty'))
		self.connection.commit()


	def getFacultyAndGroup(self, chatid):
		self.chatid = chatid
		middleList = []

		self.cursor.execute("SELECT * FROM statistic WHERE id IN (SELECT max(id) FROM statistic WHERE chatid = (%s) AND choice != (%s) AND choice != (%s) AND choice != (%s))", (self.chatid, 'news', 'feedback', 'sticker' ))

		for i, e in enumerate(self.cursor.fetchone()):
			if i == 4 or i == 5:
				middleList.append(e)

		return middleList



	def summaryVerification(self, chatid):
		self.chatid = chatid
		self.cursor.execute("SELECT groupa FROM statistic WHERE id IN (SELECT max(id) FROM statistic WHERE chatid = (%s) AND choice != (%s) AND choice != (%s) AND choice != (%s))", (self.chatid, 'news', 'feedback', 'sticker' ))

		return self.cursor.fetchone()[0]


	def updateChoice(self, choice, chatid):
		self.choice = choice
		self.chatid = chatid

		self.cursor.execute("UPDATE statistic SET choice = (%s) WHERE id IN (SELECT max(id) FROM statistic WHERE chatid = (%s) AND faculty != (%s))", (self.choice, self.chatid, 'empty'))
		self.connection.commit()


	def otherFeature(self, firstname, lastname, chatid, choice, username):
		self.firstname = firstname
		self.lastname = lastname
		self.chatid = chatid
		self.choice = choice
		self.username = username

		self.cursor.execute("INSERT INTO statistic (firstname, lastname, faculty, chatid, course, groupa, choice, username) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (self.firstname, self.lastname, 'empty', self.chatid, 'empty', 'empty', self.choice, self.username))
		self.connection.commit()

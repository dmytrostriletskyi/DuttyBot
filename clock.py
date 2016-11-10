from apscheduler.schedulers.blocking import BlockingScheduler
from bs4 import BeautifulSoup
import dj_database_url
import postgresql
import requests
import psycopg2

import datetime
import random

import utils.dataProcessing as dataProcessing
import dataLib 
import config 




sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=22, minute=1)
def dateApp():
	print ('Date app running!')
	db_info = dj_database_url.config(default=config.DBSRC)

	connection = psycopg2.connect(
	   database=db_info.get('NAME'),
	   user=db_info.get('USER'),
	   password=db_info.get('PASSWORD'),
	   host=db_info.get('HOST'),
	   port=db_info.get('PORT'))

	cursor = connection.cursor()

	cursor.execute("DROP TABLE IF EXISTS dateapp") 
	cursor.execute("CREATE TABLE IF NOT EXISTS dateapp (id serial primary key, datefirst text, datesecond text, daytoweek text);")
	

	native = datetime.datetime.now()

	firstDay = native + datetime.timedelta(hours = 2) 
	lastDay = firstDay + datetime.timedelta(days = 1) 

	dayToWeek = native + datetime.timedelta(hours = 2) 
	dayToWeek = str(dayToWeek.weekday())

	firstDay = firstDay.strftime("%d.%m")
	lastDay = lastDay.strftime("%d.%m")


	cursor.execute("INSERT INTO dateapp (datefirst, datesecond, daytoweek) VALUES (%s, %s, %s)", (firstDay, lastDay, dayToWeek))
	connection.commit()
	connection.close()




	

@sched.scheduled_job('cron', day_of_week=5, hour=3, minute=00)
def createTable():
	print ('Create table running!')
	db_info = dj_database_url.config(default=config.DBSRC)

	connection = psycopg2.connect(
	   database=db_info.get('NAME'),
	   user=db_info.get('USER'),
	   password=db_info.get('PASSWORD'),
	   host=db_info.get('HOST'),
	   port=db_info.get('PORT'))

	cursor = connection.cursor()

	cursor.execute("DROP TABLE IF EXISTS timetable") 
	cursor.execute("CREATE TABLE IF NOT EXISTS timetable (id serial primary key, faculty char(29), course char(1), groupa text, dateFirst char(5), schedule text);")
	connection.commit()


	for i in range(1, 2):

		i *= 7
		base = 6

		nativeDay = datetime.datetime.now()
		firstDay = nativeDay + datetime.timedelta(i - 5) 
		lastDay = firstDay + datetime.timedelta(base) 
		firstDay = firstDay.strftime("%d.%m.%Y")
		lastDay = lastDay.strftime("%d.%m.%Y")

		print(firstDay)
		print(lastDay)
		
		for formData in dataLib.dateToDateForm(firstDay, lastDay):
			r = requests.post(config.url, data = formData)
			soup = BeautifulSoup(r.text, 'html.parser')
			dataProcessing.dataProcessing(soup) 
		

	connection.commit()
	connection.close()

	
sched.start()






















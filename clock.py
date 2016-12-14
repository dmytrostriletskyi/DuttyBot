from apscheduler.schedulers.blocking import BlockingScheduler
from bs4 import BeautifulSoup

import dj_database_url
import requests
import psycopg2

import datetime

import utils.dataProcessing as dataProcessing
import dataLib 
import config 


sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=22)
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
	cursor.execute("INSERT INTO dateapp (done) VALUES (%s)", ('done', ))
	
	connection.commit()
	connection.close()


@sched.scheduled_job('cron', day_of_week='mon-fri', hour=22, minute=1)
def createTable():
	print ('Create everyday shedule!')
	db_info = dj_database_url.config(default=config.DBSRC)

	connection = psycopg2.connect(
	   database=db_info.get('NAME'),
	   user=db_info.get('USER'),
	   password=db_info.get('PASSWORD'),
	   host=db_info.get('HOST'),
	   port=db_info.get('PORT'))

	cursor = connection.cursor()

	cursor.execute("DELETE FROM timetable") 
	connection.commit()

	
	nativeDay = datetime.datetime.now() + datetime.timedelta() 
	weekday = datetime.datetime.today().weekday()

	firstDay = nativeDay + datetime.timedelta(-weekday) 
	lastDay = firstDay + datetime.timedelta(6) 

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


@sched.scheduled_job('cron', day_of_week=5, hour=22, minute=1)
def createTable():
	print ('Create shedule from monday to friday next weak as sunday 00:01 parser!')
	db_info = dj_database_url.config(default=config.DBSRC)

	connection = psycopg2.connect(
	   database=db_info.get('NAME'),
	   user=db_info.get('USER'),
	   password=db_info.get('PASSWORD'),
	   host=db_info.get('HOST'),
	   port=db_info.get('PORT'))

	cursor = connection.cursor()

	cursor.execute("DELETE FROM timetable") 
	connection.commit()

	
	nativeDay = datetime.datetime.now() + datetime.timedelta() 
	weekday = datetime.datetime.today().weekday()

	firstDay = nativeDay + datetime.timedelta(+2) 
	lastDay = firstDay + datetime.timedelta(6) 

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






















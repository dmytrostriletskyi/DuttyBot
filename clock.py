from apscheduler.schedulers.blocking import BlockingScheduler
from requests_to_schedule import parsing_timetable
from rutetider import Timetable, CurrentDates
from additional_data import database_url
import datetime


sched = BlockingScheduler()


def weekdays_delete():
    Timetable(database_url).clear_timetable()


def everyday_dates_refreshing():
    today = datetime.datetime.today().strftime('%d.%m.%Y')
    tomorrow = (datetime.datetime.today() + datetime.timedelta(1)).strftime('%d.%m.%Y')
    CurrentDates(database_url).add_dates(today, tomorrow)


def weekdays():
    native_day = datetime.datetime.now() + datetime.timedelta()
    weekday = datetime.datetime.today().weekday()

    first_day = native_day + datetime.timedelta(-weekday)
    last_day = first_day + datetime.timedelta(6)

    parsing_timetable(first_day.strftime("%d.%m.%Y"), last_day.strftime("%d.%m.%Y"))


def weekend_delete():
    Timetable(database_url).clear_timetable()


def weekend():
    native_day = datetime.datetime.now() + datetime.timedelta()
    weekday = datetime.datetime.today().weekday()

    first_day = native_day + datetime.timedelta(-weekday)
    last_day = first_day + datetime.timedelta(6)

    parsing_timetable(first_day.strftime("%d.%m.%Y"), last_day.strftime("%d.%m.%Y"))

sched.add_job(everyday_dates_refreshing, 'cron', day_of_week='mon-sun', hour=22)

sched.add_job(weekdays_delete, 'cron', day_of_week='mon-thu', hour=22)
sched.add_job(weekdays, 'cron', day_of_week='mon-thu', hour=22)

sched.add_job(weekend_delete, 'cron', day_of_week=5, hour=22)
sched.add_job(weekend, 'cron', day_of_week=5, hour=22)

sched.start()

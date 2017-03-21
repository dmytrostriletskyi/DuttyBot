from additional_data import group_list, schedule_url, database_url
from rutetider import Timetable
from bs4 import BeautifulSoup
import requests


def parsing_timetable(date_one, date_two):
    for group_data in group_list(date_one, date_two):
        page = requests.post(schedule_url, data=group_data)
        soup = BeautifulSoup(page.text, 'html.parser')

        schedule_table = soup.find("table", {"id": "timeTableGroup"})

        header_list = [div.text for div in soup.find_all('option', selected=True)]
        print(header_list)
        lessons_data = [div.text.replace('\r', '').replace('\n', '').replace('    ', ' ')[:-1]
                        for div in schedule_table.findAll('div', attrs={"class": "cell mh-50"})][:-2]

        lessons_date = [i.text for i in schedule_table.findAll('div') if len(i.get_text()) == 10][:-2]

        lessons_order = [str(div.text[:2]) for div in schedule_table.findAll('div',
                         attrs={"class": "mh-50 cell cell-vertical"})][:-2]

        lessons_count = [div.text.count('пара') for div in schedule_table.findAll('td') if 'пара' in div.text][:-2]
        data, order = [], []

        for count in lessons_count:
            data.append(lessons_data[:count])
            order.append([int(point) for point in lessons_order[:count]])

            lessons_data = lessons_data[count:]
            lessons_order = lessons_order[count:]

        for day, k in zip(data, order):
            store = {}
            for i in range(len(day)):
                if len(day[i]) is not 0:
                    store['lesson_order'] = i+1
                    store['lesson_title'] = day[i][:day[i].index('ауд')-1]
                    day[i] = day[i][day[i].index('ауд'):]
                    store['lesson_classroom'] = ' '.join(day[i].split()[:2])
                    store['lesson_teacher'] = ' '.join(day[i].split()[2:])
                    day[i] = store
                    store = {}

        for day, date in zip(data, lessons_date):
            for lesson in day:
                if len(lesson) is not 0:
                    if header_list[0] == 'Навчально-науковий інститут заочного та дистанційного навчання':
                        header_list[0] = 'Заочне навчання'
                    lesson['faculty'] = header_list[0]
                    lesson['course'] = header_list[1]
                    lesson['group_name'] = header_list[2]
                    lesson['lesson_date'] = date

        lessons_data_db = []

        for day in data:
            for lesson in day:
                if len(lesson) is not 0:
                    lessons_data_db.append(lesson)

        timetable = Timetable(database_url)
        timetable.create_timetable()
        for _ in lessons_data_db:
            timetable.add_lesson(_['faculty'], _['course'], _['group_name'], _['lesson_date'],
                                 _['lesson_title'], _['lesson_classroom'], _['lesson_order'], _['lesson_teacher'])

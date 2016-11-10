import psycopg2
import dj_database_url

import config as config
import utils.commitList as commitList

def dataProcessing(soup):
	mainHtmlTable = soup.find("table", {"id": "timeTableGroup"})


	# Main doing
	# Find formdata`s headers 
	headersList = [div.text for div in soup.find_all('option', selected=True)]


	# Find all schedule data
	divData = [div.text.replace("\r","").replace('\n', '').replace('    ', ' ')[:-1] \
									for div \
	 								in mainHtmlTable.findAll('div', \
	 								attrs={"class" : "cell mh-50"})][:-2]


	# Find all schedule date
	divDate = [i.text[:-5] for i in mainHtmlTable.findAll('div') if len(i.get_text()) == 10][:-2]


	# Find all schedule position in table like first lesson, second lesson etc.
	divLessons = [str(div.text[:2]) for div \
									in mainHtmlTable.findAll('div', \
									attrs={"class" : "mh-50 cell cell-vertical"})][:-2]


	# Make list of counts
	divCounts = [div.text.count('пара') for div \
										in mainHtmlTable.findAll('td') \
										if 'пара' in div.text][:-2] 


	# Pre-produce list of data
	exitDataList = list(map(lambda x, y: x + 'пара ' + y, divLessons, divData))

	# Final commit list for PostgreSQL
	dbCommitList = commitList.commitList(exitDataList, divCounts)


	if headersList[0] == 'Навчально-науковий інститут заочного та дистанційного навчання':
		headersList[0] = 'Заочне навчання'

	print (headersList)
	print (divDate)
	print (dbCommitList)
	print ()


	db_info = dj_database_url.config(default=config.DBSRC)

	connection = psycopg2.connect(
	    database=db_info.get('NAME'),
	    user=db_info.get('USER'),
	    password=db_info.get('PASSWORD'),
	    host=db_info.get('HOST'),
	    port=db_info.get('PORT'))


	cursor = connection.cursor()

	for dateInsert, lessonInsert in zip(divDate, dbCommitList):
		cursor.execute("INSERT INTO timetable (faculty, course, groupa, dateFirst, schedule) VALUES (%s, %s, %s, %s, %s)", (headersList[0], headersList[1], headersList[2], dateInsert, lessonInsert))

	connection.commit()
	connection.close()




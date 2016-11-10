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

	print (headersList[0])
	if headersList[0] == 'Навчально-науковий інститут заочного та дистанційного навчання':
		headersList[0] = 'Заочне навчання'
	print (headersList[0])
	print (headersList)
	print (divDate)
	print (dbCommitList)
	print ()






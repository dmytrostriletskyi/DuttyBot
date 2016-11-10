def commitList(exitDataList, divCounts):
	empS = ''
	dbCommitList = []
	counter = 0

	for i in range(len(divCounts)):
		for j in range(divCounts[i]):
			empS += exitDataList[counter] + ' '
			counter += 1
		dbCommitList.append(empS[:-1])
		empS = ''

	for i, e in enumerate(dbCommitList):
		if e == '1 пара ':
			dbCommitList[i] = 'Пары отсутствуют.'
		if '1 пара СвД[Доп]' in e:
			dbCommitList[i] = 'Пары отсутствуют.'
		if ', ...' in e:
			dbCommitList[i] = dbCommitList[i].replace(', ...', '')
		if 'Трембовецький ...' in e:
				dbCommitList[i] = dbCommitList[i].replace('Трембовецький ...', 'Трембовецький М.П.')
		if 'Косенко В..' in e:
				dbCommitList[i] = dbCommitList[i].replace('Косенко В..', 'Косенко И.О.')
		if 'Борсуковський ...' in e:
				dbCommitList[i] = dbCommitList[i].replace('Борсуковський ...', 'Борсуковський Ю.В.')
		if 'Оленєв Д.Г., П...' in e:
			dbCommitList[i] = dbCommitList[i].replace('Оленєв Д.Г., П...', 'Оленєв Д.Г.')
		if 'Парчевський Ю....' in e:
			dbCommitList[i] = dbCommitList[i].replace('Парчевський Ю....', 'Парчевський Ю.М.')


	return dbCommitList
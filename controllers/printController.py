import controllers.scheduleController as scheduleController
from functools import reduce

from itertools import zip_longest
from functools import reduce

import dataBaseSelections 

selectData = dataBaseSelections.dataBaseSelections()

def trimSchedule(n, schedule):
	return zip_longest(*[iter(schedule)]*n)


def printConroller(groupDB, dateDB):

	try:
		scheduleSelect = selectData.selectSchedule(groupDB, dateDB)

		if '  ' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('  ', ' ')

		if 'Мельничук  Л.В.' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('Мельничук  Л.В.', 'Мельничук Л.В.')

		if 'Василенко  Н.А.' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('Василенко  Н.А.', 'Василенко Н.А.')

		if 'ЕПДС(в ч КЕ)-1...' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('ЕПДС(в ч КЕ)-1...', 'ЕПДС')
		
		if 'Бурячок  В.Л.' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('Бурячок  В.Л.', 'Бурячок В.Л.')		

		if 'АСДС ІКБ-15[Пз]' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('АСДС ІКБ-15[Пз]', 'АСДС-ІКБ-15[Пз]')	

		if 'АСДС ІКБ-15[Лб]' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('АСДС ІКБ-15[Лб]', 'АСДС-ІКБ-15[Лб]')	

		if 'ТКС СЗІ-15[Пз]' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('ТКС СЗІ-15[Пз]', 'ТКС-СЗІ-15[Пз]')	

		if 'ТКС СЗІ-15[Лб]' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('ТКС СЗІ-15[Лб]', 'ТКС-СЗІ-15[Лб]')	

		if 'Косенко И.О., Н...' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('Косенко И.О., Н...', 'Косенко И.О.')

		if '2 пара 3 пара' in scheduleSelect:
		 	scheduleSelect = scheduleSelect.replace('2 пара 3 пара', '3 пара')

		if '3 пара 4 пара' in scheduleSelect:
		 	scheduleSelect = scheduleSelect.replace('3 пара 4 пара', '4 пара')

		if '4 пара 5 пара' in scheduleSelect:
		 	scheduleSelect = scheduleSelect.replace('4 пара 5 пара', '5 пара')

		if '5 пара 6 пара' in scheduleSelect:
		 	scheduleSelect = scheduleSelect.replace('5 пара 6 пара', '6 пара')

		if 'WEB тех.-2016[Лб]' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('WEB тех.-2016[Лб]', 'WEB-тех.-2016[Лб]')

		if 'ГВ ІПУ-2016[Сем]' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('ГВ ІПУ-2016[Сем]', 'ГВ-ІПУ-2016[Сем]')

		if 'С САПР РА-15[Лк]' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('С САПР РА-15[Лк]', 'ССАПР-РА-15[Лк]')

		if 'АСДС ІКБ-15[Лк]' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('АСДС ІКБ-15[Лк]', 'АСДС-ІКБ-15[Лк]')

		if 'Чит. зал' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('Чит. зал', 'Чит.зал')

		if 'ТАЕЗ ІКС-13[Лк]' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('ТАЕЗ ІКС-13[Лк]', 'ТАЕЗ-ІКС-13[Лк]')

		if 'ТАЕЗ ІКС-13[Пз]' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('ТАЕЗ ІКС-13[Пз]', 'ТАЕЗ-ІКС-13[Пз]')

		if 'ТСЗСЗ -13[Пз]' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('ТСЗСЗ -13[Пз]', 'ТСЗСЗ-13[Пз]')

		if 'ТСЗСЗ -13[Лк]' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('ТСЗСЗ -13[Лк]', 'ТСЗСЗ-13[Лк]')

		if 'Атременко В.О....' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('Атременко В.О....', 'Атременко В.О.')

		if 'Стецюк П.А., Г...' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('Стецюк П.А., Г...', 'Стецюк П.А.')

		if 'Гудзь О.Є., Ат...' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('Гудзь О.Є., Ат...', 'Гудзь О.Є.')

		if 'Гориня Л.М., П...' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('Гориня Л.М., П...', 'Гориня Л.М.')

		if 'ТКС СЗІ-15[Лк]' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('ТКС СЗІ-15[Лк]', 'ТКС-СЗІ-15[Лк]')

		if 'WEB тех.-2016[Лк]' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('WEB тех.-2016[Лк]', 'WEB-тех.-2016[Лк]')

		if 'ГВ ІПУ-2016[Лк]' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('ГВ ІПУ-2016[Лк]', 'ГВ-ІПУ-2016[Лк]')

		if 'С САПР РА-15[Пз]' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('С САПР РА-15[Пз]', 'С-САПР-РА-15[Пз]')

		if 'С САПР РА-15[Лб]' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('С САПР РА-15[Лб]', 'С-САПР-РА-15[Лб]')

		if 'Резерв ..' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('Резерв ..', 'Резерв .. ..')

		if 'Недашківський ...' in scheduleSelect:
			scheduleSelect = scheduleSelect.replace('Недашківський ...', 'Недашківський О.Л.')
			
		scheduleSelect = scheduleSelect.split(' ')	

	except AttributeError:
		return 'Пары отсутствуют.'

	

	try:
		if scheduleSelect == ['Пары', 'отсутствуют.']:
			return 'Пары отсутствуют.'

		schedule = [" ".join(lst) + ' ' for lst in [list(i) for i in trimSchedule(7, scheduleSelect)]]

	except BaseException:
	 	return 'Warning: it`s join`s error on the server, please, send feedback (faculty, course and group, that you chose) to me (@dmytryistriletskyi)!'

	scheduleList = []
	for field in schedule:
		objectField = scheduleController.scheduleController(field)
		field = objectField.compactData()
		scheduleList.append(field)
		scheduleList.append('\n')

	finalScheduleList = [reduce(lambda x, y: x + y, scheduleList)]


	return finalScheduleList




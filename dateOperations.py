import datetime

# today and tomorrow
native = datetime.datetime.now()

firstDay = native + datetime.timedelta(hours = 2) 
lastDay = firstDay + datetime.timedelta(days = 1) 

firstDay = firstDay.strftime("%d.%m")
lastDay = lastDay.strftime("%d.%m")




# what a week`s day?
dayToWeek = native + datetime.timedelta(hours = 2) 
dayToWeek = dayToWeek.weekday()

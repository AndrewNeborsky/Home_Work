from calendar import weekday, day_name

q = input('Enter date of your birthday in the format DD.MM.YYYY: ')
date = q.split('.')

week = weekday(int(date[2]), int(date[1]), int(date[0]))

print('The day of the week you were born is', day_name[week])

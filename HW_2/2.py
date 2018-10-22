import calendar
from datetime import date as data

q = input('Введите дату вашего рождения в формате DD.MM.YYYY: ')
date = q.split('.')

d = {calendar.day_name[0]: 0, calendar.day_name[1]: 1, calendar.day_name[2]: 2, calendar.day_name[3]: 3,
     calendar.day_name[4]: 4, calendar.day_name[5]: 5, calendar.day_name[6]: 6}

week = calendar.weekday(int(date[2]), int(date[1]), int(date[0]))

print('День недели в который вы родились это --', calendar.day_name[week])

wd = input('Введите название недели: ')

now = str(data.today()).split('-')

w = (None, None)
i = int(now[1]) + 1
j = int(now[0])
while w[0] != d[wd]:
    if i > 12:
        i = 1
        j += 1
    w = calendar.monthrange(j, i)
    i += 1

print('Ближайший месяц и год, когда этот день недели выпадал на 1-ое число это --', calendar.month_name[i-1], j)

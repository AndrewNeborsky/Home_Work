from calendar import day_name, month_name, monthrange
from datetime import date

wd = input('Enter the name of the day: ')
d = {day_name[0]: 0, day_name[1]: 1, day_name[2]: 2, day_name[3]: 3,
     day_name[4]: 4, day_name[5]: 5, day_name[6]: 6}

now = str(date.today()).split('-')

w = (None, None)
i = int(now[1]) + 1
j = int(now[0])

while w[0] != d[wd]:
    if i > 12:
        i = 1
        j += 1
    w = monthrange(j, i)
    i += 1

print('The month and year, when this day will gotten on the 1st is', month_name[i-1], j)

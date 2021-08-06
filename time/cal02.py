import calendar

c = calendar.TextCalendar()
year = 2020
month = 1

for date in c.itermonthdates(year, month):
    print(date)
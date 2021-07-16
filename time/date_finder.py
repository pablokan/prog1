date_strings = [
    "March 12 2010",
    "2010-03-12",
    "03/12/2010 12:42:12"
]

from datefinder import find_dates as fDate
date_dates = [list(fDate(d)) for d in date_strings]
print(date_dates)

for fecha in fDate('june 3 of 1965'):
    print(fecha)
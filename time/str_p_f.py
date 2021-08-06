from datetime import datetime

#The strptime() method creates a datetime object from a given string.
date_string = "1 August, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object, type(date_object))

#The strftime() method returns a string representing date and time using date, time or datetime object.
now = datetime.now()
year = now.strftime("%Y")
print("year:", year, type(year))

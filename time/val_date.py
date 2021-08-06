from datetime import datetime

goodDate = False
while not goodDate:
    testDate = input("Enter a date in DD-MM-YYYY format: ")
    try:
        goodDate = bool(datetime.strptime(testDate, "%d-%m-%Y"))
    except:
        print("Invalid date format")


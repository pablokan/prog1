from datetime import datetime, date

def dt2d(dt):
    return date(dt.year, dt.month, dt.day)

def inputDate(msg):
    goodDate = False
    while not goodDate:
        testDate = input(f"{msg}: ")
        try:
            goodDate = datetime.strptime(testDate, "%d-%m-%Y")
        except:
            print("Invalid date format")
    return goodDate

if __name__ == "__main__":
    f = inputDate('Fecha de check-in')
    print(f"{f} aceptada", type(f))
    print(f.strftime("%d-%m-%Y"))
    print(dt2d(f), type(dt2d(f)))



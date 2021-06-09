a = open("t01.txt", "r")

c = " "

while c !="": # control de fin de archivo
    c = a.read(1)
    if c != chr(10):
        print(c)

a.close()

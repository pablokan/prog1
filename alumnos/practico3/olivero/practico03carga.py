def carga(nombres,fechasDeNacimiento):
    times=int(input("How many dates of birth do you wish to enter?: "))
    for x in range (times):
        namein=input("Enter the name of the person: ")
        nombres.append(namein)
        birthdiny=input("Enter the date of birth(dd/mm/yyyy): ")
        fechasDeNacimiento.append(birthdiny) 

names=[]
birthDate=[]

carga(names,birthDate)
f=open("a.txt","w")
for i in range(len(names)):
    f.write(names[i])
    f.write("\n")
    f.write(birthDate[i])
    f.write("\n")
f.close()








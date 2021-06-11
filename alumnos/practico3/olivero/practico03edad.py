from datetime import date
def edad(fn):
    hoy = date.today()
    dn, mn, an = fn.split('/')
    dn = int(dn)
    mn = int(mn)
    an = int(an)
    dh = hoy.day
    mh = hoy.month
    ah = hoy.year
    e = ah - an
    if (mn > mh) or (mn == mh and dn > dh):
        e -= 1
    return e

names=[]
birthDate=[]

f=open("a.txt","r") 
linea=" "

while linea !="":
    linea=f.readline()
    linea=linea[:-1]
    if "/" in linea:
         birthDate.append(linea)
    else:
        names.append(linea) 

for x in range (len(birthDate)):
    if edad(birthDate[x])>=18:
        print(names[x])    




def f2(a):
    ap = " "
    for x in a:
      if x not in ",":
         ap += x
    return ap
 
listanombres = []
 
for x in range(7):
   nombre = input("introduzca su nombre: ")
   listanombres.append(nombre)
   v = nombre[0]
   apell = input("introduzca su apellido: ")
   listapellidos = []
   listapellidos.append(apell)
   print(v + "." + f2(apell))
 
print(listanombres)
 
c = 0
maslarga = " "
for x in listanombres:
   if len(x) > c:
      c = (len(x))
      maslarga = (x)
 
print("el nombre mas largo es: " , maslarga)
 
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
 
def foo():
    h = date.today()
    print(h)
 
foo()
 
if __name__ == '__main__':
    print(edad("02/05/1943"))
    print(edad("07/09/1984"))
    print(edad("21/12/1967"))
    print(edad("30/08/1995"))
    
    promedio = (78 + 36 + 53 + 25)/4
    print(promedio)
    
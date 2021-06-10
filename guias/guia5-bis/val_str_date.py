# def edad(fn): # parámetro en formato str dd-mm-aaaa

from datetime import datetime
fn = '31-06-1991'

dn, mn, an = fn.split('-')
print(dn, mn, an)
isDate = False
try:
    datetime(int(an), int(mn), int(dn))
    isDate = True
except:
    print('fecha no válida')


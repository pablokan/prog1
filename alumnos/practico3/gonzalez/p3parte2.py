from datetime import date
def edad(fn):
    hoy = date.today()
    dn, mn, an = fn.split('-')
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

t = open('nyf.txt', 'r')
p = t.readlines()
t.close()
p0 = p[0]
p1 = p[1]
p1 = p1.split(',')
p0 = p0.split(',')

for x in range(len(p0[:-1])):
    if edad(p1[x]) >= 18:
        print(p0[x], 'es mayor de edad')
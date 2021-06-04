from datetime import date
def edad(fn):
    hoy = date.today()
    #print(hoy)
    #print('mes',hoy.month)    # fecha precisa del momento 
    dn, mn, an = fn.split('-')
    dn = int(dn)
    mn = int(mn)
    an = int(an)
    dh = hoy.day
    mh = hoy.month
    ah = hoy.year
    years = ah - an
    if (mn > mh) or (mn == mh and dn > dh):
        years -= 1
    return years

def foo():
    h = date.today()
    print(h)

foo()

if __name__ == '__main__':
    print(edad('15-07-1999'))
   
    
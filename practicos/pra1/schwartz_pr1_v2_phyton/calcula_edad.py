def edad(fn):
    from datetime import date
    hoy = date.today()
    dn,mn,an = fn.split('/')
    dn = int(dn)
    mn= int(mn)
    an= int(an)
    dh= hoy.day
    mh = hoy.month
    ah = hoy.year
    e = ah - an
    if (mn > mh) or (mn == mh and dn > dh):
        e -=1
    return e


if __name__=='__main__':
    print(edad('30-12-1983'))







#nacimiento n
dn, nm, an= 30, 12, 1983

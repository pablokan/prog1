def edad(fecha_nacimiento):
    from datetime import date
    hoy = date.today()
    dia_nacimiento = fecha_nacimiento.split('/')
    mes_nacimiento = fecha_nacimiento.split('/')
    ano_nacimiento = fecha_nacimiento.split('/')
    dia_nacimiento = int(dia_nacimiento)
    mes_nacimiento = int(mes_nacimiento)
    ano_nacimiento = int(ano_nacimiento)
    dia_hoy = hoy.day
    mes_hoy = hoy.month
    ano_hoy = hoy.year
    e = ano_hoy - ano_nacimiento
    if (mes_nacimiento > mes_hoy) or (mes_nacimiento == mes_hoy and dia_nacimiento > dia_hoy):
        e -= 1
    return e
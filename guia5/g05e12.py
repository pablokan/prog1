# 12. Cargar en listas los nombres y fechas de nacimiento de varias personas, 
# luego recorrerlo y mostrar los nombres de los mayores de edad. 
# Funciones de carga y cálculo de edad.

from calcula_edad import edad

def carga():
    nombres = ['Juan', 'Luisa', 'Ana', 'Pedro']
    fecNac = ['07-02-2004', '13-09-1991', '17-10-2012', '04-04-1963']
    return nombres, fecNac

n, f = carga()

for x in range(len(n)):
    if edad(f[x]) >= 18:
        print(n[x], 'tiene', edad(f[x]))

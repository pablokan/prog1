# 7. Almacenar en dos  listas paralelas, nombres y sexos 
# de 8 personas. Al finalizar, recorrerlas y mostrar 
# los nombres de las mujeres. 
# Dos funciones: carga y mostrarMujeres

def carga():
    nombres = []
    sexos = []
    for x in range(3):
        nombre = input('Nombre: ')
        nombres.append(nombre)
        sexo = input('Sexo: ')
        sexos.append(sexo)
    return nombres, sexos

def mostrarMujeres(n, s):
    for x in range(len(n)):
        if s[x] == 'f':
            print(n[x])

no, se = carga()
print('Las mujeres son:')
mostrarMujeres(no, se)



# Realizar una aplicación que maneje una Lista de Tareas.
# Deben decidir que categorías utilizar (ej: trabajo, estudio, personal, etc.), el manejo del tiempo 
# (fechas, urgencias, límites temporales, etc.)
# También deben decidir que estructuras de datos usar, listas y/o diccionarios y/o archivos de texto, etc.
# Agregar la mayor cantidad de variantes útiles posible!
# Es obligatorio implementar el práctico con la estructura trabajada en la clase del 3 de agosto (ver 
# comentarios en las Novedades)
from datetime import datetime

def encabezado():
    f=datetime.now()
    dia = f.day
    mes = f.month
    año = f.year
    
    print("\n******************************")
    print("\t¡¡To Do List!!")
    print("******************************")
    print("     Hoy es:",dia, "-", mes, "-", año)
    print("******************************\n")

def verRegistroDeActividades(): # Necesito ver la lista de actividades guardadas
    # Tarea,Categoria,Fecha (Orden de datos almacenados)
    archivo = open("to_do_list.txt")
    linea = " "
    while linea != "":
        linea = archivo.readline() # Leo por linea
        coma = linea.find(",") # Busco la coma
        nombre = linea[:coma] # Consegui el primer elemento (tarea)
        print(linea[-11:-1], nombre)
    archivo.close()
    """ 
    archivo = open("to_do_list.txt", "r")
    lineas = archivo.readlines()
    for li in lineas:
        print(li.strip("\n"))
    archivo.close() 
    """
    return menu()
    
def agregarActividad(tarea,categoria,fecha): # Necesito guardar los datos
    file = open("to_do_list.txt","a")
    file.write("\n" + tarea + "," + categoria + "," + fecha)
    file.close()

def actividadParaHoy():
    fecha = datetime.now().strftime("%Y/%m/%d") # año, mes y dia
    fechaStr = str(fecha)
    archivo = open("to_do_list.txt")
    f = " "
    while f != "":
        f = archivo.readline()
        if fechaStr in f:
            print(f)
    archivo.close()

def menu():
    encabezado()
    print(">>>Bienvenido a su Asistente Virtual<<<\n")
    print("Menú de Opciones\n")
    print("1) Registrar Actividad")
    print("2) Ver Lista de Actividades")
    print("3) Actividades para Hoy")
    print("4) Salir\n")
    opcion = input(">>> ")
    
    if opcion == "1":
        tarea = input("Ingrese nombre de la actividad: ")
        categoria = input("Ingrese tipo de actividad (tarea,compra,examen,etc):")
        fecha = input("Ingrese fecha de la actividad (aaaa/mm/dd): ")
        agregarActividad(tarea,categoria,fecha)
        print("Actividad completada...")
        return menu()
    elif opcion == "2":
        print("Actividades registradas: ")
        verRegistroDeActividades()
        return menu()
    elif opcion == "3":
        print("Actividades para Hoy: ")
        actividadParaHoy()
        return menu()
    elif opcion == "4":
        print("\nExit..\n")
        exit()


if __name__ == '__main__':
    menu()
    

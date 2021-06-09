archivo = open('t02.txt','w') # modo sobreescritura, si no existe se crea
archivo.write("Python es divertido y ")
segundaLinea = "Java es aburrido mal" + "\n" 
archivo.write(segundaLinea) 
archivo.close()

archivo = open('t02.txt','a') # modo agregar
archivo.writelines(["Hasta la vista baby!\n", "Me fui.\n"])  
lista = ["hola", "y", "chau"]

archivo.writelines(lista)
archivo.close()

class Persona():
    especie = "humana" # atributo de clase
    def __init__(self, nombre, edad): # Constructor (se ejecuta al crear un objeto)
        self.nombre = nombre # atributo de instancia
        self.edad = edad # self representa al objeto en sí mismo

    def obtenerDatos(self): # método
        return self.nombre, self.edad

# instanciaciones (instancia = objeto)
persona1 = Persona('John', 33) # Se crea un objeto de la clase Persona
persona2 = Persona('Jane', 22) # los argumentos los recibe el constructor
print(persona1.obtenerDatos())
print(persona2.nombre) # Se accede a los atributos de la clase violando el encapsulamiento


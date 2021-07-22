class Animal:
    """A generic animal"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, newage):
        self.age = newage

    def __str__(self):
        return "animal:" + self.name + "->" + str(self.age)

gato = Animal("Tom", 3)
print(gato)
print(gato.get_name(), "es", gato.get_age())
gato.set_age(5)
print(gato.get_name(), "es", gato.get_age())

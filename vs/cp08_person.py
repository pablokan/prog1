from dataclasses import dataclass

@dataclass
class Persond():
    name: str
    age: int

    def __str__(self):
        return f"{self.name} is {self.age} years old."

p1 = Persond("John", 36)
print(p1)

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getData(self):
        return f"{self.name} is {self.age} years old."


p2 = Person("Paul", 63)
print(p2.getData())

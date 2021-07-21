from dataclasses import dataclass

@dataclass
class Car:
    color: str
    brand: str
    model: str
    year: int = 2021
    price: float = 0.0
    def __str__(self):
        return f"{self.color} {self.brand} {self.model} {self.year} {self.price}"

auto = Car(color="red", brand="Toyota", model="Corolla", year=2017, price=33000)
print(auto)

@dataclass
class Person:
    name: str
    age: int
    def __str__(self):
        return f"{self.name} {self.age}"

p = Person('Anne', 'doce') # typing not enforce, just warning
print(p)

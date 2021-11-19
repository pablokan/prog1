def foo(par):
    if par > 87:
        pass
    else:
        return 1


# comment
n, s = 91, "hola"
li = [3, "chau", True, None, (2, 3), int]
di = {"name": "John"}
f = foo(n)

from dataclasses import dataclass


@dataclass
class Persona:
    name: str
    age: int

    def saludo(self):
        print(f"Hola {self.name}, tenés {self.age} años")

    def __str__(self) -> str:
        return f"{self.name} tiene {self.age} años"


p = Persona("Paul", 56)
p.saludo()
print(p)
print(f"\N{Sauropod}")

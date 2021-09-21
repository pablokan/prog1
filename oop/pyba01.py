from dataclasses import dataclass

@dataclass(frozen=True, repr=False)
class Dog:
    name: str
    age: int

    species: str = 'Canis familiaris' 

p1 = Dog("Buddy", 7, "qqqqq")

print(p1)


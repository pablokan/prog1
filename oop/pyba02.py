from dataclasses import dataclass, field

@dataclass
class Materia:
    title: str = field(compare=False)
    comment: str = field(init=False, repr=False, default='Sin comentarios')
    language : str = field(default='Python3')
    value : int = 11   

materia1 = Materia('Lengua', 'Irrelevante')
materia2 = Materia("Programación")

print(materia1) 
print(materia2) 
print(materia1 == materia2)

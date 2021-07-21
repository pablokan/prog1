from dataclasses import dataclass
from pydantic.dataclasses import dataclass as pyd_dataclass
from pydantic import BaseModel
@dataclass
class Foo:
    number: int

@pyd_dataclass
class Bar:
    number: int

class Model(BaseModel):
    number: int

# f1 = Foo(number = 1.4)
# f2 = Foo(number = '1.4')
# print(f1, f2)

b1 = Bar(number = 1.4)
# b2 = Bar(number = '1.4')
print(b1)

m1 = Model(number = 1.4)
# m2 = Model(number = '1.4')
print(m1)

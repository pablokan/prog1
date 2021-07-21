from pydantic import BaseModel

class Model(BaseModel):
    a: int
    b: str

m = Model(a='1.1', b='2')
print(m)

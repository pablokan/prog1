from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from datetime import date

class baseVars(BaseModel):
    age: int = 10
    name: str = 'John Doe'
    birth: date = date(1990, 1, 1)

v = baseVars()
v.age = "20 años"
print(v.dict())





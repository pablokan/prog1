from pydantic import BaseModel
from typing import Tuple


class Model(BaseModel):
    tuple_of_different_types: Tuple[int, float, str, bool]


print(Model(tuple_of_different_types=[4.1, "3", 2, 1]).tuple_of_different_types)

Model.tuple_of_different_types = (1, 1.1, "", 9)

print(Model.tuple_of_different_types)

from dataclasses import dataclass
from pydantic import BaseModel
@dataclass
class MyData(BaseModel):
    n1:int
    n2:int
    result:int

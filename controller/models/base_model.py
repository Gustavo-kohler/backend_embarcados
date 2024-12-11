from pydantic import BaseModel
from typing import Union

class Planta_base(BaseModel):
    id: Union[int, None] = None
    nome: Union[str, None] = None
    umidade_max: Union[int, None] = None
    umidade_min: Union[int, None] = None
    luz_max: Union[int, None] = None
    luz_min: Union[int, None] = None

class Config_base(BaseModel):
    tempo_verif: Union[int, None] = None
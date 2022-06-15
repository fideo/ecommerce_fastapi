from sqlite3 import Date
from typing import Any, List, Optional
from pydantic import BaseModel, Field
from datetime import datetime

class Categoria(BaseModel):
    categoria_id: Optional[int]
    nombre_categoria: str
    descripcion: str
    esta_activo: bool
    class Config:
        orm_mode = True

class ActualizarCategoria(BaseModel):
    nombre_categoria: str
    descripcion: str
    esta_activo: bool
    class Config:
        orm_mode = True

class EliminarCategoria(BaseModel):
    categoria_id: int
    mensaje: str
    class Config:
        orm_mode = True
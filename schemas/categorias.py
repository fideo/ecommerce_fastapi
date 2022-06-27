from sqlite3 import Date
from typing import Any, List, Optional
from pydantic import BaseModel, Field
from datetime import datetime

class CategoriaBase(BaseModel):
    nombre_categoria: str
    descripcion: str
    
    class Config:
        orm_mode = True

class CategoriaCreate(CategoriaBase):
    pass

class Categoria(CategoriaBase):
    categoria_id: int

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


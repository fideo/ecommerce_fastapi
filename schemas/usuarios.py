from sqlite3 import Date
from typing import Any, List, Optional
from pydantic import BaseModel, Field
from datetime import datetime

class UsuarioBase(BaseModel):
    
    username: str
    
class UsuarioCreate(UsuarioBase):
    password: str

class Usuario(UsuarioBase):
    id: int
    esta_activo: bool
    
    class Config:
        orm_mode = True

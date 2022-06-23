from this import s
from sqlite3 import Date
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Any, List, Optional,Union

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None

class UsuarioBase(BaseModel):
    nombre_de_usuario: str
    correo_de_usuario: str
    pais: str
    ciudad: str

class UsuarioCreate(UsuarioBase):
    contrasenia_encriptada: str

class Usuario(UsuarioBase):
    usuario_id: int
    esta_activo: Union[bool,None] = None
    class Config:
        orm_mode = True

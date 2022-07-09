from pydantic import BaseModel, EmailStr
from typing import Union

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None

class UsuarioBase(BaseModel):
    nombre_de_usuario: str
    correo_de_usuario: EmailStr
    pais: str
    ciudad: str

class UsuarioCreate(UsuarioBase):
    contrasenia_encriptada: str

class Usuario(UsuarioBase):
    usuario_id: int
    
    class Config:
        orm_mode = True

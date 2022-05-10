from typing import Optional
from pydantic import BaseModel

class UsuarioBase(BaseModel):
    correo_de_vendedor: str

class UsuarioCreate(UsuarioBase):
    password: str

class Usuario(UsuarioBase):
    usuario_id: int
    esta_activo: bool    
    class Config:
        orm_mode = True

class VendedorBase(BaseModel):
    correo_de_usuario: str

class VendedorCreate(VendedoresBase):
    password: str

class Vendedor(VendedoresBase):
    vendedor_id: int
    esta_activo: bool
    productos_publicados: list[Producto] = []
    class Config:
        orm_mode = True

class ProductoBase(BaseModel):
    titulo: str
    descripcion: Optional[str] = None

class ProductoCreate(ProductoBase):
    pass

class Producto(ProductoBase):
    producto_id: int
    vendedor_del_producto_id: int
    class Config:
        orm_mode = True    

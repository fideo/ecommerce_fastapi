from sqlite3 import Date
from typing import List, Optional
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


class VendedorBase(BaseModel):
    correo_de_usuario: str


class VendedorCreate(VendedorBase):
    password: str


class Vendedor(VendedorBase):
    vendedor_id: int
    esta_activo: bool
    productos_publicados: List[Producto] = []

    class Config:
        orm_mode = True


class VentasBase(BaseModel):
    fecha_venta: Date
    numero_de_productos_comprados: int
    precio_total_de_venta: float
    producto_id: int


class Ventas(VentasBase):
    venta_id: int

    class Config:
        orm_mode = True

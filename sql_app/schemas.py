from sqlite3 import Date
from typing import Any, List, Optional
from pydantic import BaseModel, Field
from datetime import datetime


class UsuarioBase(BaseModel):
    correo_de_vendedor: str


class UsuarioCreate(UsuarioBase):
    password: str


class VentaBase(BaseModel):
    fecha_venta: Date
    numero_de_productos_comprados: int
    precio_total_de_venta: float
    producto_id: int

    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
        __pydantic_self__.fecha_venta = Date()


class VentaCreate(VentaBase):
    pass

class ProductoBase(BaseModel):
    nombre_producto: str
    fecha_de_publicacion: datetime
    numero_de_productos_subidos: int
    precio_unitario_de_producto: int
    descripcion: Optional[str] = None


class ProductoCreate(ProductoBase):
    pass


class VendedorBase(BaseModel):
    correo_de_vendedor: str
    pais: str
    nombre: str
    ciudad: str


class VendedorCreate(VendedorBase):
    constraseña_encriptada: str


class VentaBase(BaseModel):
    fecha_venta: Date
    numero_de_productos_comprados: int
    precio_total_de_venta: float
    producto_id: int

    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
        __pydantic_self__.fecha_venta = Date()


class VentaCreate(VentaBase):
    pass


class Vendedor(VendedorBase):
    vendedor_id: int
    esta_activo: bool
    productos: List[ProductoBase] = []

    class Config:
        orm_mode = True


class Usuario(UsuarioBase):
    usuario_id: int
    esta_activo: bool

    class Config:
        orm_mode = True


class Producto(ProductoBase):
    producto_id: int
    vendedores : List[VendedorBase] = []
    
    class Config:
        orm_mode = True


class Venta(VentaBase):
    venta_id: int
    productos: List[VendedorBase] = []

    class Config:
        orm_mode = True

from sqlite3 import Date
from typing import Any, List, Optional
from pydantic import BaseModel
from datetime import datetime

# Inicio schema de Usuario
class UsuarioBase(BaseModel):
    correo_de_vendedor: str


class UsuarioCreate(UsuarioBase):
    password: str


class Usuario(UsuarioBase):
    usuario_id: int
    esta_activo: bool

    class Config:
        orm_mode = True
# Fin schema de Usuario

# Inicio schema de Producto
class ProductoBase(BaseModel):
    nombre_producto: str
    fecha_de_publicacion: datetime
    numero_de_productos_subidos: int
    precio_unitario_de_producto: int
    descripcion: Optional[str] = None


class ProductoCreate(ProductoBase):
    pass


class Producto(ProductoBase):
    producto_id: int
    vendedor_del_producto_id: int

    class Config:
        orm_mode = True
# Fin schema de Producto

# Inicio schema de Categoría
class CategoriaBase(BaseModel):
    categoria_id: int
    nombre_categoria: str

class CategoriaCreate(CategoriaBase):
    pass


class Categoria(CategoriaBase):
    categoria_id: int
    categoria_del_producto_id: int

    class Config:
        orm_mode = True

# Fin schema de Categoría

# Inicio schema de Vendedor
class VendedorBase(BaseModel):
    correo_de_vendedor: str
    pais: str
    nombre: str
    ciudad: str
    
    
class VendedorCreate(VendedorBase):
    constraseña_encriptada: str

class Vendedor(VendedorBase):
    vendedor_id: int
    esta_activo: bool
    productos_publicados: List[Producto] = []

    class Config:
        orm_mode = True


class VentaBase(BaseModel):
    fecha_venta: Date
    numero_de_productos_comprados: int
    precio_total_de_venta: float
    producto_id: int

    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
        __pydantic_self__.fecha_venta = Date()

# Fin schema de Vendedor

# Inicio schema de Venta
class VentaCreate(VentaBase):
    pass


class Venta(VentaBase):
    venta_id: int

    class Config:
        orm_mode = True
# Fin schema de Venta
from sqlite3 import Date
from typing import Any, List, Optional
from pydantic import BaseModel, Field
from datetime import datetime




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

    class Config:
        orm_mode = True


# Inicio schema de Producto
class ProductoBase(BaseModel):
    nombre_producto: str
    fecha_de_publicacion: datetime
    numero_de_productos_subidos: int
    link_de_imagen: str
    precio_unitario_de_producto: int
    descripcion: Optional[str] = None
    class Config:
        orm_mode = True


class ProductoCreate(ProductoBase):
    pass


class Producto(ProductoBase):
    producto_id: Optional[int]

    class Config:
        orm_mode = True
# Fin schema de Producto

# Inicio schema de Categoría
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

# Fin schema de Categoría

# Inicio schema de Vendedor

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


# Inicio schema de Usuario
class UsuarioBase(BaseModel):
    correo: str
class UsuarioCreate(UsuarioBase):
    password: str

class Usuario(UsuarioBase):
    usuario_id: int
    esta_activo: bool
    class Config:
        orm_mode = True

# Fin schema de Usuario

class Producto(ProductoBase):
    producto_id: int
    vendedores : List[UsuarioBase] = []
    
    class Config:
        orm_mode = True


class Venta(VentaBase):
    venta_id: int
    productos: List[ProductoBase] = []

    class Config:
        orm_mode = True
# Fin schema de Venta

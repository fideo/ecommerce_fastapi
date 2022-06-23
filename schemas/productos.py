from sqlite3 import Date
from typing import Any, List, Optional
from pydantic import BaseModel, Field
from datetime import datetime

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
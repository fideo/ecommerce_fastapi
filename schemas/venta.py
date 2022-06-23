from sqlite3 import Date
from typing import Any, List, Optional
from pydantic import BaseModel, Field
from datetime import datetime
from .productos import ProductoBase

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

class Venta(VentaBase):
    venta_id: int
    productos: List[ProductoBase] = []

    class Config:
        orm_mode = True
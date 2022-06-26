from typing import List
from pydantic import BaseModel
from datetime import datetime


class VentaProducto(BaseModel):
    producto_id: int
    cantidad: int


class VentaProductoBase(BaseModel):
    venta_id: int
    producto_id: int
    cantidad: int
    precio_unitario: float


class VentaCreate(BaseModel):
    venta_productos: List[VentaProducto] = []


class Venta(BaseModel):
    venta_id: int
    fecha_venta: datetime
    venta_productos: List[VentaProducto] = []

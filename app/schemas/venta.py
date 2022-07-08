from typing import List
from pydantic import BaseModel
from datetime import datetime


class VentaProductoCreate(BaseModel):
    producto_id: int
    cantidad: int


class Producto(BaseModel):
    nombre_producto: str
    link_de_imagen: str
    descripcion: str

    class Config:
        orm_mode = True


class VentaProducto(BaseModel):
    producto: Producto
    precio_unitario: float
    cantidad: int

    class Config:
        orm_mode = True


class Venta(BaseModel):
    venta_id: int
    fecha_venta: datetime
    ventas_productos: List[VentaProducto] = []
    precio_total: float

    class Config:
        orm_mode = True

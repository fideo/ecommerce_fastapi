from sqlite3 import Date
from typing import Any, List, Optional
from pydantic import BaseModel, Field
from datetime import datetime
from schemas import categorias 
#from schemas import venta

class ProductoBase(BaseModel):
    nombre_producto: str
    fecha_de_publicacion: datetime
    numero_de_productos_subidos: int
    stock: int
    link_de_imagen: str
    precio_unitario_de_producto: int
    descripcion: Optional[str] = None
    class Config:
        orm_mode = True


class ProductoCreate(ProductoBase): 
    numero_de_categorias: int
    categorias: List[str]#Optional[str] = None

class Producto(ProductoBase):
    producto_id: int

    class Config:
        orm_mode = True

    
"""class VentaDeProducto(BaseModel):
    venta: venta.Venta
    producto: Producto
    cantidad: int
"""

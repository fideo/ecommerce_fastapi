from typing import List
from sqlalchemy.orm import Session
from schemas import ventas as ventas_schemas
from models.venta import Venta, VentaProducto
from models.producto import Producto
import datetime


def crear_venta(
    db: Session,
    venta_productos: List[ventas_schemas.VentaProducto],
) -> ventas_schemas.Venta:
    now = datetime.datetime.now()
    db_venta = Venta(fecha_de_venta=now)
    db.add(db_venta)
    db.flush()

    for venta_producto in venta_productos:
        producto = db.query(Producto).filter(Producto.id == venta_producto.id).first()
        db_venta_producto = VentaProducto(
            venta_id=db_venta.id,
            producto_id=producto.id,
            cantidad=venta_producto.cantidad,
            precio_unitario=producto.precio_unitario,
        )
        db.add(db_venta_producto)

    db.commit()
    db.refresh(db_venta)

    return db_venta


def obtener_venta_por_id(db: Session, venta_id: int) -> ventas_schemas.Venta:
    db_venta = db.query(Venta).get(venta_id)
    return db_venta


def obtener_ventas(db: Session) -> List[ventas_schemas.Venta]:
    ventas = db.query(Venta).all()
    return ventas

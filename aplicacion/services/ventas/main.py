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
    db_venta = Venta(fecha_venta=now)
    db.add(db_venta)
    db.flush()

    for venta_producto in venta_productos:
        producto = (
            db.query(Producto)
            .filter(Producto.producto_id == venta_producto.producto_id)
            .first()
        )
        db_venta_producto = VentaProducto(
            venta_id=db_venta.venta_id,
            producto_id=producto.producto_id,
            cantidad=venta_producto.cantidad,
            precio_unitario=producto.precio_unitario_de_producto,
        )
        db.add(db_venta_producto)

        producto.numero_de_productos_subidos = (
            producto.numero_de_productos_subidos - venta_producto.cantidad
        )
        db.add(producto)

    db.commit()
    db.refresh(db_venta)

    return db_venta


def obtener_venta_por_id(db: Session, venta_id: int) -> ventas_schemas.Venta:
    db_venta = db.query(Venta).get(venta_id)
    return db_venta


def obtener_ventas(db: Session) -> List[ventas_schemas.Venta]:
    ventas = db.query(Venta).all()
    return ventas

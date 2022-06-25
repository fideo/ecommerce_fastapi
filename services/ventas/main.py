from typing import List
from sqlalchemy.orm import Session
from sql_app import schemas, models


def crear_ventas(db: Session, venta: schemas.VentaCreate) -> schemas.Venta:
    db_venta = models.Venta(
        fecha_de_venta=venta.fecha_venta,
        numero_de_productos_comprados=venta.numero_de_productos_comprados,
        precio_total_de_venta=venta.precio_total_de_venta,
        producto_id=venta.producto_id,
    )
    db.add(db_venta)
    db.commit()
    db.refresh(db_venta)

    return db_venta


def obtener_venta_por_id(db: Session, venta_id: int) -> schemas.Venta:
    db_venta = db.query(models.Venta).get(venta_id)
    return db_venta


def obtener_ventas(db: Session) -> List[schemas.Venta]:
    ventas = db.query(models.Venta).all()
    return ventas

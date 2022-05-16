from typing import List
from sqlalchemy.orm import Session
from ..sql_app import schemas, models


class ServicioVentas:
    def __init__(self, db: Session) -> None:
        self.db = db

    def crear_ventas(self, venta: schemas.VentaCreate) -> schemas.Venta:
        db_venta = models.Venta(
            fecha_de_venta=venta.fecha_venta,
            numero_de_productos_comprados=venta.numero_de_productos_comprados,
            precio_total_de_venta=venta.precio_total_de_venta,
            producto_id=venta.producto_id,
        )
        self.db.add(db_venta)
        self.db.commit()
        self.db.refresh(db_venta)

        return db_venta

    def obtener_venta_por_id(self, venta_id: int) -> schemas.Venta:
        db_venta = self.db.query(models.Venta).get(venta_id)
        return db_venta

    def obtener_ventas(self) -> List[schemas.Venta]:
        ventas = self.db.query(models.Venta).all()
        return ventas

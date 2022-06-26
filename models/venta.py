from sqlalchemy import (
    Column,
    Float,
    ForeignKey,
    Integer,
    DateTime,
)
from sql_app.database import Base
from sqlalchemy.orm import relationship


class Venta(Base):
    __tablename__ = "ventas"

    venta_id = Column(Integer, primary_key=True, index=True)
    fecha_venta = Column(DateTime)
    ventas_productos = relationship("VentaProducto")

    @property
    def precio_total(self):
        return sum(
            [venta_producto.precio_total() for venta_producto in self.ventas_productos]
        )


class VentaProducto(Base):
    __tablename__ = "ventas_productos"
    venta_id = Column(ForeignKey("ventas.venta_id"), primary_key=True)
    producto_id = Column(ForeignKey("productos.producto_id"), primary_key=True)
    precio_unitario = Column(Float)
    cantidad = Column(Integer)

    producto = relationship("Producto")

    def precio_total(self):
        return self.precio_unitario * self.cantidad

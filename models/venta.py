from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, Date, DateTime, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from sql_app.database import Base

class Venta(Base):
    __tablename__ = "ventas"

    venta_id = Column(Integer, primary_key=True, index=True)
    fecha_de_venta = Column(Date)
    @property
    def productos(self):
        s = """
            SELECT temp.* FROM (
                SELECT
                    productos.*,
                    ventas_de_productos.precio_unitario,
                    ventas_de_productos.cantidad,
                    ventas_de_productos.producto_id
                FROM productos INNER JOIN ventas_de_productos ON productos.producto_id = ventas_de_productos.producto_id
            ) AS temp
            INNER JOIN ventas ON temp.venta_id = ventas.venta_id
            WHERE ventas.venta_id = :ventaid
            """
        result = object_session(self).execute(s,params={"ventaid":self.venta_id}).fetchall()
        return result

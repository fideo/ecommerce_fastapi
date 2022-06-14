from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, Date, DateTime, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from sql_app.database import Base

class Producto(Base):
    __tablename__ = "productos"

    producto_id = Column(Integer, primary_key=True, index=True)
    nombre_producto = Column(String,nullable=False)
    fecha_de_publicacion = Column(DateTime)
    numero_de_productos_subidos = Column(Integer)
    precio_unitario_de_producto = Column(Integer)
    link_de_imagen = Column(String,nullable=False)
    descripcion = Column(String)

    @property
    def ventas(self):
        s = """
            SELECT temp.* FROM (
                SELECT
                    ventas.*,
                    ventas_de_productos.precio_unitario,
                    ventas_de_productos.cantidad,
                    ventas_de_productos.venta_id
                FROM ventas INNER JOIN ventas_de_productos ON ventas.venta_id = ventas_de_productos.venta_id
            ) AS temp
            INNER JOIN productos ON temp.producto_id = productos.producto_id
            WHERE productos.producto_id = :productoid
            """
        result = object_session(self).execute(s,params={"productoid":self.producto_id}).fetchall()
        return result

    categorias = relationship(
            "Categoria",
            secondary = "categorias_de_productos",
            back_populates = "productos"
    )
from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, Date, DateTime, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from .database import Base


vendedores_de_productos = Table('vendedores_de_productos', Base.metadata,
    Column('vendedor_id', ForeignKey('vendedores.vendedor_id'), primary_key=True),
    Column('producto_id', ForeignKey('productos.producto_id'), primary_key=True)
)

#ventas_de_productos = Table('ventas_de_productos', Base.metadata,
#    Column('ventas_id', ForeignKey('ventas.venta_id'), primary_key=True),
#    Column('producto_id', ForeignKey('productos.producto_id'), primary_key=True)
#)

categorias_de_productos = Table("categorias_de_productos", Base.metadata,
    Column("categoria_id", ForeignKey("categorias.categoria_id"), primary_key=True),
    Column("producto_id", ForeignKey("productos.producto_id"), primary_key=True),
)

#class VendedorDeProducto(Base):
#    __tablename__ = "vendedores_de_productos"
#    vendedor_id = Column(ForeignKey('vendedores.vendedor_id'), primary_key=True)
#    producto_id = Column(ForeignKey('productos.producto_id'), primary_key=True)
#    extra = Column(String, nullable=False)
#    vendedor = relationship("Vendedor", back_populates="productos")
#    producto = relationship("Producto", back_populates="vendedores")
#
#    nombre_de_vendedor = association_proxy(target_collection="vendedor",
#                                attr="nombre")
#    nombre_de_producto = association_proxy(target_collection="producto",
#                                attr="nombre_producto")
#
#
class VentaDeProducto(Base):
    __tablename__ = "ventas_de_productos"
    venta_id = Column(ForeignKey('ventas.venta_id'),
                         primary_key=True)
    producto_id = Column(ForeignKey('productos.producto_id'),
                            primary_key=True)
    precio_unitario = Column(Float)
    cantidad = Column(Integer)

class Vendedor(Base):
    __tablename__ = "vendedores"

    vendedor_id = Column(Integer, primary_key=True, index=True)
    correo_de_vendedor = Column(String, unique=True)
    nombre = Column(String,nullable=False)
    contraseña_encriptada = Column(String)
    pais = Column(String)
    ciudad = Column(String)
    esta_activo = Column(Boolean)
    productos = relationship(
        "Producto",
        secondary="vendedores_de_productos",
        back_populates="vendedores"
    )

class Categoria(Base):
    __tablename__ = "categorias"

    categoria_id = Column(Integer, primary_key=True, index=True)
    nombre_categoria = Column(String, unique=True)
    descripcion = Column(String)
    esta_activo = Column(Boolean)
    productos = relationship(
        "Producto",
        secondary="categorias_de_productos",
        back_populates="categorias"
        )


class Producto(Base):
    __tablename__ = "productos"

    producto_id = Column(Integer, primary_key=True, index=True)
    nombre_producto = Column(String,nullable=False)
    fecha_de_publicacion = Column(DateTime)
    numero_de_productos_subidos = Column(Integer)
    precio_unitario_de_producto = Column(Integer)
    descripcion = Column(String)
    vendedores = relationship(
            "Vendedor",
            secondary="vendedores_de_productos",
            back_populates="productos")
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


class Venta(Base):
    __tablename__ = "ventas"

    venta_id = Column(Integer, primary_key=True, index=True)
    fecha_de_venta = Column(Date)
    #numero_de_productos_comprados = Column(Integer,nullable=False)
    #precio_total_de_venta = Column(Float)
    #precio_total_de_venta = #agregar @aggregated(.....
    #productos = relationship(
    #        "Producto",
    #        secondary="ventas_de_productos",
    #        back_populates="ventas")
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

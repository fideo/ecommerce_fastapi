from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, Date, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy 
from .database import Base


vendedores_de_productos = Table('vendedores_de_productos', Base.metadata,
    Column('vendedor_id', ForeignKey('vendedores.vendedor_id'), primary_key=True),
    Column('producto_id', ForeignKey('productos.producto_id'), primary_key=True)
)

ventas_de_productos = Table('ventas_de_productos', Base.metadata,
    Column('ventas_id', ForeignKey('ventas.venta_id'), primary_key=True),
    Column('producto_id', ForeignKey('productos.producto_id'), primary_key=True)
)

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
#class VentaDeProducto(Base):
#    __tablename__ = "ventas_de_productos"
#    venta_id = Column(ForeignKey('ventas.venta_id'), primary_key=True)
#    producto_id = Column(ForeignKey('productos.producto_id'), primary_key=True)
#    precio_unitario = Column(Float)
#    cantidad = Column(Integer)
#    #blurb = Column(String, nullable=False)
#    venta = relationship("Venta", back_populates="productos")
#    producto = relationship("Producto", back_populates="ventas")
#
#    precio_total_de_venta = association_proxy(target_collection="venta",
#                                attr="precio_total_de_venta")
#    nombre_de_producto = association_proxy(target_collection="producto",
#                                attr="nombre_producto")
    


class Usuario(Base):
    __tablename__ = "usuarios"

    usuario_id = Column(Integer, primary_key=True, index=True)
    correo_de_usuario = Column(String, unique=True)
    contraseña_encriptada = Column(String)
    pais = Column(String)
    esta_activo = Column(Boolean)
    ciudad = Column(String)


class Vendedor(Base):
    __tablename__ = "vendedores"

    vendedor_id = Column(Integer, primary_key=True, index=True)
    correo_de_vendedor = Column(String, unique=True)
    nombre = Column(String)
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
    nombre_producto = Column(String)
    fecha_de_publicacion = Column(Date)
    numero_de_productos_subidos = Column(Integer)
    precio_unitario_de_producto = Column(Integer)
    vendedores = relationship(
            "Vendedor",
            secondary="vendedores_de_productos",
            back_populates="productos")
    ventas = relationship(
            "Venta",
            secondary="ventas_de_productos",
            back_populates="productos")
    categorias = relationship(
            "Categoria",
            secondary = "categorias_de_productos",
            back_populates = "productos"
    )


class Venta(Base):
    __tablename__ = "ventas"

    venta_id = Column(Integer, primary_key=True, index=True)
    fecha_de_venta = Column(Date)
    numero_de_productos_comprados = Column(Integer)
    #precio_total_de_venta = #agregar @aggregated(.....
    productos = relationship(
            "Producto",
            secondary="ventas_de_productos",
            back_populates="ventas")

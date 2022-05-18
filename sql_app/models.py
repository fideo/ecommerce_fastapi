from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from .database import Base



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
    descripcion = Column(String)
    productos_publicados = relationship(
        "Producto", back_populates="vendedor_del_producto"
    )


class Producto(Base):
    __tablename__ = "productos"

    producto_id = Column(Integer, primary_key=True, index=True)
    nombre_producto = Column(String)
    fecha_de_publicacion = Column(Date)
    numero_de_productos_subidos = Column(Integer)
    precio_unitario_de_producto = Column(Integer)
    vendedor_del_producto_id = Column(Integer, ForeignKey("Vendedor.vendedor_id"))
    vendedor_del_producto = relationship(
        "Vendedor", back_populates="productos_publicados"
    )


"""class Venta(Base):
    __tablename__ = "ventas"

    venta_id = Column(Integer, primary_key=True, index=True)
    fecha_de_venta = Column(Date)
    numero_de_productos_comprados = Column(Integer)
    precio_total_de_venta = Column(Float)
    producto_id = Column(Integer, ForeignKey("Producto.producto_id"))
    producto = relationship("Producto", back_populates="ventas_realizadas")
"""

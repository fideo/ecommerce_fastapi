from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, Date, DateTime, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from sql_app.database import Base

class Categoria(Base):
    __tablename__ = "categorias"

    categoria_id = Column(Integer, primary_key=True, index=True)
    nombre_categoria = Column(String, unique=True)
    descripcion = Column(String)
    #esta_activo = Column(Boolean)
    productos = relationship(
        "CategoriaProducto",
        #secondary="categorias_de_productos",
        back_populates="categoria"
        )


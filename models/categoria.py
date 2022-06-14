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

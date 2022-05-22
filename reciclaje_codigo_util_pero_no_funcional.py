class VendedorDeProducto(Base):
    __tablename__ = "vendedores_de_productos"
    vendedor_id = Column(ForeignKey('vendedores.vendedor_id'), primary_key=True)
    producto_id = Column(ForeignKey('productos.producto_id'), primary_key=True)
    extra = Column(String, nullable=False)
    vendedor = relationship("Vendedor", back_populates="productos")
    producto = relationship("Producto", back_populates="vendedores")

    nombre_de_vendedor = association_proxy(target_collection="vendedor",
                                attr="nombre")
    nombre_de_producto = association_proxy(target_collection="producto",
                                attr="nombre_producto")


class VentaDeProducto(Base):
    __tablename__ = "ventas_de_productos"
    venta_id = Column(ForeignKey('ventas.venta_id'), primary_key=True)
    producto_id = Column(ForeignKey('productos.producto_id'), primary_key=True)
    #blurb = Column(String, nullable=False)
    venta = relationship("Venta", back_populates="productos")
    producto = relationship("Producto", back_populates="ventas")

    precio_total_de_venta = association_proxy(target_collection="venta",
                                attr="precio_total_de_venta")
    nombre_de_producto = association_proxy(target_collection="producto",
                                attr="nombre_producto")

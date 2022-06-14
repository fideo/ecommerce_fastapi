from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, Date, DateTime, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from sql_app.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    usuario_id = Column(Integer, primary_key=True, index=True)
    correo_de_usuario = Column(String, unique=True)
    contraseña_encriptada = Column(String)
    pais = Column(String)
    esta_activo = Column(Boolean)
    ciudad = Column(String)
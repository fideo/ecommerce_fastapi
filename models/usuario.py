from sqlalchemy import Boolean, Column, Integer, String
from sql_app.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    usuario_id = Column(Integer, primary_key=True, index=True)
    nombre_de_usuario = Column(String,unique=True)
    correo_de_usuario = Column(String, unique=True)
    contrasenia_encriptada = Column(String)
    pais = Column(String)
    esta_activo = Column(Boolean, default=True)
    ciudad = Column(String)
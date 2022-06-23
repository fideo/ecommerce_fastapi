from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, Date, DateTime, Table
from sql_app.database import Base


class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, default=None)
    #email = Column(String, unique=True, index=True)
    password = Column(String)
    esta_activo = Column(Boolean, default=True)
#    pais = Column(String)
#    ciudad = Column(String)
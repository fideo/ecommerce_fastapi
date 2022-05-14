from sqlalchemy.orm import Session
from . import models, schemas

def obtener_usuario(db: Session, usuario_id: int):
    return db.query

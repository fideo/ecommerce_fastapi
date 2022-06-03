from typing import List
from sqlalchemy.orm import Session
from sql_app import models, schemas
from dependencies import get_db
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

@router.get("/", tags=["usuarios"], response_model=List[schemas.Usuario])
def obtener_usuarios(db: Session = Depends(get_db)):
  usuario = db.query(models.Usuario).all()
  return usuario
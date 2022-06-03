from typing import List
from sqlalchemy.orm import Session
from sql_app import models, schemas
from dependencies import get_db
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/categorias", tags=["categorias"])

@router.get("/", tags=["categorias"], response_model=List[schemas.Categoria])
def obtener_categorias(db: Session = Depends(get_db)):
    categoria = db.query(models.Categoria).all()
    return categoria
from typing import List
from sqlalchemy.orm import Session
from sql_app import models, schemas
from dependencies import get_db
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/categorias")

def obtener_categorias(db: Session = Depends(get_db)):
    categoria = db.query(models.Categoria).all()
    return categoria

@router.get('/')
def mostrar_categorias(db: Session = Depends(get_db)):
    categoria = obtener_categorias(db=db)
    context = {
        "categorias": categoria
    }
    return context

from typing import List
from sqlalchemy.orm import Session
from sql_app import models, schemas
from dependencies import get_db
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/productos", tags=["productos"])

@router.get("/", tags=["productos"], response_model=List[schemas.Producto])
def obtener_productos(db: Session = Depends(get_db)):
    producto = db.query(models.Producto).all()
    return producto

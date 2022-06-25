from typing import List

from dependencies import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services.ventas.main import obtener_ventas, obtener_venta_por_id, crear_venta
import schemas

router = APIRouter(prefix="/ventas", tags=["ventas"])


@router.get("/", response_model=List[schemas.Venta])
async def obtener_ventas(db: Session = Depends(get_db)):
    ventas = obtener_ventas(db)
    return ventas


@router.get("/{id}", response_model=schemas.Venta)
async def obtener_venta(id: int, db: Session = Depends(get_db)):
    venta = obtener_venta_por_id(db, id)
    return venta


@router.post("/", response_model=schemas.Venta)
async def crear_venta(venta: schemas.VentaCreate, db: Session = Depends(get_db)):
    venta = crear_venta(db, venta)
    return venta

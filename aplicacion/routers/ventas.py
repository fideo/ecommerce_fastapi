from typing import List

from dependencies import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..services.ventas import ServicioVentas
from ..sql_app import schemas

router = APIRouter(prefix="/ventas", tags=["ventas"])


@router.get("/", response_model=List[schemas.Venta])
async def obtener_ventas(db: Session = Depends(get_db)):
    ventas = ServicioVentas(db).obtener_ventas()
    return ventas


@router.get("/{id}", response_model=schemas.Venta)
async def obtener_venta(id: int, db: Session = Depends(get_db)):
    venta = ServicioVentas(db).obtener_venta_por_id(id)
    return venta


@router.post("/", response_model=schemas.Venta)
async def crear_venta(venta: schemas.VentaCreate, db: Session = Depends(get_db)):
    venta = ServicioVentas(db).crear_venta(venta)
    return venta

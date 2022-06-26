from typing import List

from dependencies import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services.ventas import main as ServicioVentas
from schemas.ventas import Venta, VentaProducto

router = APIRouter(prefix="/ventas", tags=["ventas"])


@router.get("/", response_model=List[Venta])
async def obtener_ventas(db: Session = Depends(get_db)):
    ventas = ServicioVentas.obtener_ventas(db)
    return ventas


@router.get("/{id}", response_model=Venta)
async def obtener_venta(id: int, db: Session = Depends(get_db)):
    venta = ServicioVentas.obtener_venta_por_id(db, id)
    return venta


@router.post("/", response_model=Venta)
async def crear_venta(
    venta_productos: List[VentaProducto], db: Session = Depends(get_db)
):
    venta = ServicioVentas.crear_venta(db, venta_productos)
    return venta

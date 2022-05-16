from fastapi import APIRouter

router = APIRouter(prefix="/ventas", tags=["ventas"])


@router.get("/")
async def obtener_ventas():
    return {"ventas": "ventas"}


@router.get("/{id}")
async def obtener_venta(id: int):
    return {"venta": f"venta {id}"}


@router.post("/")
async def crear_venta():
    return {"ventas": "ventas"}

from typing import List
from urllib import request

from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sql_app import models,schemas
from sql_app.database import SessionLocal, engine
from sqlalchemy.orm import Session
from dependencies import get_db
from routers.productos import main as productos_router
from routers.categorias import main as categorias_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/')
async def index(request: Request):
  context = {
    "request": request,
  }
  return templates.TemplateResponse("index.html", context)

templates = Jinja2Templates(directory="templates")

app.include_router(productos_router.router)

app.include_router(categorias_router.router)


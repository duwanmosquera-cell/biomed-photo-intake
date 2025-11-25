from fastapi import FastAPI
from app.database import Base, engine
from app.routes import router

app = FastAPI()

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

# Incluir rutas
app.include_router(router)
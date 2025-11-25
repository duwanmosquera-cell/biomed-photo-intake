from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .database import get_db
from .models import EquipoDB

router = APIRouter()

# Modelo de entrada para crear equipos
class EquipoCreate(BaseModel):
    nombre: str
    modelo: str
    serie: str
    fecha_pm: str

@router.post("/equipo", response_model=dict)
def registrar_equipo(equipo: EquipoCreate, db: Session = Depends(get_db)):
    # Validar que la serie no esté repetida
    existente = db.query(EquipoDB).filter(EquipoDB.serie == equipo.serie).first()
    if existente:
        raise HTTPException(status_code=400, detail="Ya existe un equipo con esa serie")

    equipo_db = EquipoDB(**equipo.dict())
    db.add(equipo_db)
    db.commit()
    db.refresh(equipo_db)
    return {"estado": "registrado", "datos": {
        "id": equipo_db.id,
        "nombre": equipo_db.nombre,
        "modelo": equipo_db.modelo,
        "serie": equipo_db.serie,
        "fecha_pm": equipo_db.fecha_pm
    }}

@router.get("/equipos", response_model=list
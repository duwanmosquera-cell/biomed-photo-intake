from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    # Relación con dispositivos
    devices = relationship("Device", back_populates="owner")


class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    # Relación con usuario
    owner = relationship("User", back_populates="devices")
    # Relación con mediciones
    measurements = relationship("Measurement", back_populates="device")


class Measurement(Base):
    __tablename__ = "measurements"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(Float, nullable=False)
    unit = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    device_id = Column(Integer, ForeignKey("devices.id"))

    # Relación con dispositivo
    device = relationship("Device", back_populates="measurements")
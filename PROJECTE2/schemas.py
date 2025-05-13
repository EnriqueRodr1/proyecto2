from pydantic import BaseModel
from typing import List, Optional
from datetime import date, time

# Esquemas para Socios
class SocioCreate(BaseModel):
    nombre: Optional[str] = None
    telefono: Optional[str] = None
    email: str
    dni: Optional[str] = None
    contrasenya: str

class SocioResponse(BaseModel):
    id: int
    nombre: Optional[str] = None
    telefono: Optional[str] = None
    email: str
    dni: Optional[str] = None

    class Config:
        orm_mode = True

# Esquemas para Hoteles
class HotelCreate(BaseModel):
    nombre: Optional[str] = None
    ubicacion: Optional[str] = None
    disponibilidad: Optional[bool] = True
    valoracion: Optional[float] = None

class HotelResponse(BaseModel):
    id: int
    nombre: Optional[str] = None
    ubicacion: Optional[str] = None
    disponibilidad: Optional[bool] = True
    valoracion: Optional[float] = None

    class Config:
        orm_mode = True

# Esquemas para Habitaciones
class HabitacionCreate(BaseModel):
    hotel_id: int
    tipo: Optional[str] = None
    disponibilidad: Optional[bool] = True

class HabitacionResponse(BaseModel):
    id: int
    hotel_id: int
    tipo: Optional[str] = None
    disponibilidad: Optional[bool] = True

    class Config:
        orm_mode = True

# Esquemas para Restaurantes
class RestauranteCreate(BaseModel):
    nombre: Optional[str] = None
    ubicacion: Optional[str] = None
    valoracion: Optional[float] = None
    descripcion: Optional[str] = None
    disponibilidad: Optional[bool] = True

class RestauranteResponse(BaseModel):
    id: int
    nombre: Optional[str] = None
    ubicacion: Optional[str] = None
    valoracion: Optional[float] = None
    descripcion: Optional[str] = None
    disponibilidad: Optional[bool] = True

    class Config:
        orm_mode = True

# Esquemas para Pistas
class PistaCreate(BaseModel):
    nombre: Optional[str] = None
    tipo: Optional[str] = None
    ubicacion: Optional[str] = None
    disponibilidad: Optional[bool] = True
    valoracion: Optional[float] = None

class PistaResponse(BaseModel):
    id: int
    nombre: Optional[str] = None
    tipo: Optional[str] = None
    ubicacion: Optional[str] = None
    disponibilidad: Optional[bool] = True
    valoracion: Optional[float] = None

    class Config:
        orm_mode = True

# Esquemas para Spa
class SpaCreate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    ubicacion: Optional[str] = None
    disponibilidad: Optional[bool] = True
    valoracion: Optional[float] = None

class SpaResponse(BaseModel):
    id: int
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    ubicacion: Optional[str] = None
    disponibilidad: Optional[bool] = True
    valoracion: Optional[float] = None

    class Config:
        orm_mode = True

# Esquemas para Reservas de Hotel
class ReservaHotelCreate(BaseModel):
    socio_id: int
    habitacion_id: int
    fecha_entrada: date
    fecha_salida: date

class ReservaHotelResponse(BaseModel):
    id: int
    socio_id: int
    habitacion_id: int
    fecha_entrada: date
    fecha_salida: date

    class Config:
        orm_mode = True

# Esquemas para Reservas de Pista
class ReservaPistaCreate(BaseModel):
    socio_id: int
    pista_id: int
    fecha: date

class ReservaPistaResponse(BaseModel):
    id: int
    socio_id: int
    pista_id: int
    fecha: date

    class Config:
        orm_mode = True

# Esquemas para Reservas de Restaurante
class ReservaRestauranteCreate(BaseModel):
    socio_id: int
    restaurante_id: int
    fecha: date
    hora: time

class ReservaRestauranteResponse(BaseModel):
    id: int
    socio_id: int
    restaurante_id: int
    fecha: date
    hora: time

    class Config:
        orm_mode = True

# Esquemas para Reservas de Spa
class ReservaSpaCreate(BaseModel):
    socio_id: int
    spa_id: int
    fecha: date
    hora: time

class ReservaSpaResponse(BaseModel):
    id: int
    socio_id: int
    spa_id: int
    fecha: date
    hora: time

    class Config:
        orm_mode = True

# Esquemas para Favoritos
class FavoritoCreate(BaseModel):
    socio_id: int
    tipo: str
    referencia_id: int
    fecha_agregado: date

class FavoritoResponse(BaseModel):
    id: int
    socio_id: int
    tipo: str
    referencia_id: int
    fecha_agregado: date

    class Config:
        orm_mode = True

# Esquemas para Locales Populares
class LocalPopularCreate(BaseModel):
    local_id: int
    popularidad: float

class LocalPopularResponse(BaseModel):
    id: int
    local_id: int
    popularidad: float

    class Config:
        orm_mode = True
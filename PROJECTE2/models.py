from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

# Socios
class Socio(Base):
    __tablename__ = "socios"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    nombre = Column(String)
    contraseña = Column(String)
    reservas = relationship("Reserva", back_populates="socio")
    favoritos = relationship("Favorito", back_populates="socio")

    # Relaciones
    reservas_hotel = relationship("ReservaHotel", back_populates="socio")
    reservas_pistas = relationship("ReservaPista", back_populates="socio")
    reservas_restaurante = relationship("ReservaRestaurante", back_populates="socio")
    reservas_spa = relationship("ReservaSpa", back_populates="socio")
    favoritos = relationship("Favorito", back_populates="socio")

# Hotg(100), nullable=True)
    ubicacion = Column(Text, nullable=True)
    disponibilidad = Column(Boolean, default=True)
    valoracion = Column(Float, nullable=True)

    # Relaciones
    habitaciones = relationship("Habitacion", back_populates="hotel")
    reservas_hotel = relationship("ReservaHotel", back_populates="hotel")

class Habitacion(Base):
    __tablename__ = 'habitaciones'

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey('hoteles.id'))
    tipo = Column(String(50), nullable=True)
    disponibilidad = Column(Boolean, default=True)

    # Relaciones
    hotel = relationship("Hotel", back_populates="habitaciones")
    reservas_hotel = relationship("ReservaHotel", back_populates="habitacion")

# Restaurantes
class Restaurante(Base):
    __tablename__ = 'restaurantes'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=True)
    ubicacion = Column(Text, nullable=True)
    valoracion = Column(Float, nullable=True)
    descripcion = Column(Text, nullable=True)
    disponibilidad = Column(Boolean, default=True)

    # Relaciones
    servicios = relationship("ServicioRestaurante", back_populates="restaurante")
    reservas_restaurante = relationship("ReservaRestaurante", back_populates="restaurante")

class ServicioRestaurante(Base):
    __tablename__ = 'servicio_restaurante'

    id = Column(Integer, primary_key=True, index=True)
    restaurante_id = Column(Integer, ForeignKey('restaurantes.id'))
    tipo_menu = Column(String(50), nullable=True)
    tipo_cocina = Column(String(100), nullable=True)
    ambiente = Column(String(100), nullable=True)
    terraza = Column(Boolean, default=False)

    # Relación con Restaurante
    restaurante = relationship("Restaurante", back_populates="servicios")

# Pistas
class Pista(Base):
    __tablename__ = 'pistas'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=True)
    tipo = Column(String(50), nullable=True)
    ubicacion = Column(Text, nullable=True)
    disponibilidad = Column(Boolean, default=True)
    valoracion = Column(Float, nullable=True)

    # Relaciones
    servicios = relationship("ServicioPistas", back_populates="pista")
    reservas_pistas = relationship("ReservaPista", back_populates="pista")

class ServicioPistas(Base):
    __tablename__ = 'servicio_pistas'

    id = Column(Integer, primary_key=True, index=True)
    pista_id = Column(Integer, ForeignKey('pistas.id'))
    tipo_pista = Column(String(50), nullable=True)
    numero_personas = Column(Integer, nullable=True)
    material = Column(String(100), nullable=True)
    tiempo_disponible = Column(String(50), nullable=True)

    # Relación con Pista
    pista = relationship("Pista", back_populates="servicios")

# Spa
class Spa(Base):
    __tablename__ = 'spa'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=True)
    descripcion = Column(Text, nullable=True)
    ubicacion = Column(Text, nullable=True)
    disponibilidad = Column(Boolean, default=True)
    valoracion = Column(Float, nullable=True)

    # Relaciones
    servicios = relationship("ServicioSpa", back_populates="spa")
    reservas_spa = relationship("ReservaSpa", back_populates="spa")

class ServicioSpa(Base):
    __tablename__ = 'servicio_spa'

    id = Column(Integer, primary_key=True, index=True)
    spa_id = Column(Integer, ForeignKey('spa.id'))
    tipo_servicio = Column(String(100), nullable=True)
    duracion = Column(Integer, nullable=True)

    # Relación con Spa
    spa = relationship("Spa", back_populates="servicios")

# Reservas

class Reserva(Base):
    __tablename__ = "reservas"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("socios.id"))
    lugar_id = Column(Integer)
    fecha = Column(Date)
    socio = relationship("Socio", back_populates="reservas")


class ReservaHotel(Base):
    __tablename__ = 'reservas_hotel'

    id = Column(Integer, primary_key=True, index=True)
    socio_id = Column(Integer, ForeignKey('socios.id'))
    hotel_id = Column(Integer, ForeignKey('hoteles.id'))  # Nueva columna para la relación directa con Hotel
    habitacion_id = Column(Integer, ForeignKey('habitaciones.id'))
    fecha_entrada = Column(Date, nullable=True)
    fecha_salida = Column(Date, nullable=True)

    # Relaciones
    socio = relationship("Socio", back_populates="reservas_hotel")
    hotel = relationship("Hotel", back_populates="reservas_hotel")  # Relación directa con Hotel
    habitacion = relationship("Habitacion", back_populates="reservas_hotel")

class ReservaPista(Base):
    __tablename__ = 'reservas_pistas'

    id = Column(Integer, primary_key=True, index=True)
    socio_id = Column(Integer, ForeignKey('socios.id'))
    pista_id = Column(Integer, ForeignKey('pistas.id'))
    fecha = Column(Date, nullable=True)

    # Relaciones
    socio = relationship("Socio", back_populates="reservas_pistas")
    pista = relationship("Pista", back_populates="reservas_pistas")

class ReservaRestaurante(Base):
    __tablename__ = 'reservas_restaurante'

    id = Column(Integer, primary_key=True, index=True)
    socio_id = Column(Integer, ForeignKey('socios.id'))
    restaurante_id = Column(Integer, ForeignKey('restaurantes.id'))
    fecha = Column(Date, nullable=True)
    hora = Column(Time, nullable=True)

    # Relaciones
    socio = relationship("Socio", back_populates="reservas_restaurante")
    restaurante = relationship("Restaurante", back_populates="reservas_restaurante")

class ReservaSpa(Base):
    __tablename__ = 'reservas_spa'

    id = Column(Integer, primary_key=True, index=True)
    socio_id = Column(Integer, ForeignKey('socios.id'))
    spa_id = Column(Integer, ForeignKey('spa.id'))
    fecha = Column(Date, nullable=True)
    hora = Column(Time, nullable=True)

    # Relaciones
    socio = relationship("Socio", back_populates="reservas_spa")
    spa = relationship("Spa", back_populates="reservas_spa")

# Favoritos
class Favorito(Base):
    __tablename__ = "favoritos"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("socios.id"))
    referencia_id = Column(Integer)
    socio = relationship("Socio", back_populates="favoritos")

    # Relación con Socio
    socio = relationship("Socio", back_populates="favoritos")

# Locales Populares
class LocalPopular(Base):
    __tablename__ = 'locales_populares'

    id = Column(Integer, primary_key=True, index=True)
    local_id = Column(Integer, nullable=False)
    popularidad = Column(Float, nullable=False)  # Cambiado a FLOAT
# crud.py
from sqlalchemy.orm import Session
import models, schemas
import bcrypt

# -------- SOCIOS --------

def crear_socio(db: Session, socio: schemas.SocioCreate):
    hashed_password = bcrypt.hashpw(socio.contrasenya.encode('utf-8'), bcrypt.gensalt())
    db_socio = models.Socio(
        nombre=socio.nombre,
        telefono=socio.telefono,
        email=socio.email,
        contrasenya=hashed_password.decode('utf-8')
    )
    db.add(db_socio)
    db.commit()
    db.refresh(db_socio)
    return db_socio


def autenticar_socio(db: Session, email: str, contrasenya: str):
    socio = db.query(models.Socio).filter_by(email=email).first()
    if not socio:
        return None
    if bcrypt.checkpw(contrasenya.encode('utf-8'), socio.contrasenya.encode('utf-8')):
        return socio
    return None

# -------- FAVORITOS --------

def crear_favorito(db: Session, favorito: schemas.FavoritoCreate):
    db_favorito = models.Favorito(**favorito.dict())
    db.add(db_favorito)
    db.commit()
    db.refresh(db_favorito)
    return db_favorito


def obtener_favoritos(db: Session, email: str):
    return db.query(models.Favorito).filter(models.Favorito.email == email).all()


def eliminar_favorito(db: Session, favorito_id: int):
    favorito = db.query(models.Favorito).filter_by(id=favorito_id).first()
    if favorito:
        db.delete(favorito)
        db.commit()

# -------- PAGOS --------

def registrar_pago(db: Session, pago: schemas.PagoCreate):
    db_pago = models.Pago(**pago.dict())
    db.add(db_pago)
    db.commit()
    db.refresh(db_pago)
    return db_pago

# -------- RESERVAS --------

def eliminar_reserva(db: Session, reserva_id: int):
    reserva = db.query(models.ReservaHotel).filter_by(id=reserva_id).first()
    if reserva:
        db.delete(reserva)
        db.commit()

    reserva_spa = db.query(models.ReservaSpa).filter_by(id=reserva_id).first()
    if reserva_spa:
        db.delete(reserva_spa)
        db.commit()

    reserva_pista = db.query(models.ReservaPista).filter_by(id=reserva_id).first()
    if reserva_pista:
        db.delete(reserva_pista)
        db.commit()

    reserva_restaurante = db.query(models.ReservaRestaurante).filter_by(id=reserva_id).first()
    if reserva_restaurante:
        db.delete(reserva_restaurante)
        db.commit()


# -------- RESERVAS SPA --------
def crear_reserva_spa(db: Session, reserva: schemas.ReservaSpaCreate):
    db_reserva = models.ReservaSpa(**reserva.dict())
    db.add(db_reserva)
    db.commit()
    db.refresh(db_reserva)
    return db_reserva


# -------- RESERVAS PISTA --------
def crear_reserva_pista(db: Session, reserva: schemas.ReservaPistaCreate):
    db_reserva = models.ReservaPista(**reserva.dict())
    db.add(db_reserva)
    db.commit()
    db.refresh(db_reserva)
    return db_reserva

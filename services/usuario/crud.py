from sqlalchemy.orm import Session
from models import usuario as usermod
from schemas import usuarios as userschem
import datetime
import hashlib

def get_password_hashed(password):
    return hashlib.sha256(bytes(password, 'utf-8')).hexdigest()

def get_user(db: Session, user_id: int):
    return db.query(usermod.Usuario).filter(usermod.Usuario.id == user_id).first()

#def get_user_by_email(db: Session, email: str):
    #return db.query(models.Usuario).filter(models.Usuario.email == email).first()

def get_user_by_username(db: Session,username: str):
    return db.query(usermod.Usuario).filter(usermod.Usuario.username == username).first()
  
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(usermod.Usuario).offset(skip).limit(limit).all()

def create_user(db: Session,  user: userschem.UsuarioCreate): # pendienre arreglar conflito en los atributos username y email de la base de datos
    hashed_password = get_password_hashed(user.password)
    db_user = usermod.Usuario(username=user.username, password=hashed_password) 
    db.add(db_user) 
    db.commit() 
    db.refresh(db_user)
    return db_user

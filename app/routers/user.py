from fastapi import APIRouter, Depends
from app.schemas import User, UserID, ShowUser, UpdateUser
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import models
from typing import List

router = APIRouter(
    prefix = '/user',
    tags = ["User"]
)




@router.get('', response_model=List[ShowUser])
def Obtener_Usuarios(db: Session = Depends(get_db)):
    data = db.query(models.User).all()
    
    return data

@router.post('')
def Crear_Usuario(user: User, db: Session = Depends(get_db)):
    usuario = user.dict()
    nuevo_usuario = models.User(
        username = usuario['username'],
        password = usuario['password'],
        nombre = usuario['nombre'],
        apellido = usuario['apellido'],
        direccion = usuario['direccion'],
        telefono = usuario['telefono'],
        correo = usuario['correo']
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return{"Usuario Creado Correctamente!"}

@router.post('/{user_id}', response_model= ShowUser)
def Obtener_Usuario_ID(user_id:int, db: Session = Depends(get_db)):
    usuario = db.query(models.User).filter(models.User.id == user_id).first()
    if not usuario:    
        return {"respuesta":"Usuario no encontrado"}
    return usuario

@router.delete('/{user_id}')
def Eliminar_Usuario(user_id :int, db: Session = Depends(get_db)):
    usuario = db.query(models.User).filter(models.User.id == user_id)
    if not usuario.first():    
        return {"respuesta":"Usuario no encontrado"}
    usuario.delete(synchronize_session = False)
    db.commit()
    return {"respuesta":"Usuario Eliminado Correctamente!"}

@router.patch('/{user_id}')
def Actualizar_Usuario(user_id :int, updateUser: UpdateUser, db: Session = Depends(get_db)):
        usuario = db.query(models.User).filter(models.User.id == user_id)
        if not usuario.first():    
            return {"respuesta":"Usuario no encontrado"}
        usuario.update(updateUser.dict(exclude_unset= True))
        db.commit()
        return {"respuesta":"Usuario Actualizado Correctamente!"}

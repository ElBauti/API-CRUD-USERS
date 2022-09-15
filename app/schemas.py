from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    username:str
    password:str
    nombre:str
    apellido:str
    direccion: Optional[str]
    telefono:int
    correo:str
    creacion_user:datetime = datetime.now()


class UpdateUser(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    direccion: Optional[str]
    telefono: Optional[int] = None
    correo: Optional[str] = None

class UserID(BaseModel):
    id:int

class ShowUser(BaseModel):
    username:str
    nombre:str
    apellido:str
    correo:str
    class Config():
        orm_mode = True
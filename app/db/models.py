import datetime
from email.policy import default
from app.db.database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True, autoincrement = True)
    username = Column(String, unique = True)
    password =  Column(String, unique = True)
    nombre = Column(String) 
    apellido = Column(String)
    direccion =  Column(String)
    telefono =  Column(Integer)
    correo = Column(String, unique = True)
    creacion_user = Column(DateTime, default= datetime.now, onupdate = datetime.now)
    estado = Column(Boolean, default = False)
    venta = relationship("Venta", backref = "usuario", cascade = 'delete,merge')
    
class Venta(Base):
    __tablename__ = 'venta'
    id = Column(Integer, primary_key = True, autoincrement = True)
    usuario_id = Column(Integer, ForeignKey("user.id", ondelete = 'CASCADE'))
    venta = Column(Integer)
    ventas_productos = Column(Integer)
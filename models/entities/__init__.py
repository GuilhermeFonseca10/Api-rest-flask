from .Usuarios import Usuarios
from config import db

__all__ = [
 
  'Usuarios'
]

db.create_all()
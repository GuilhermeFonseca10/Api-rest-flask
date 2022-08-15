from .Lojas import Lojas
from .Produtos import Produtos
from config import db

__all__ = [
 
  'Lojas'
  'Produtos'
]

db.create_all()
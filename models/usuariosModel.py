from config import db
from .entities import Usuarios
from flask import jsonify, request

def get_all():
  addrs = Usuarios.query.all()
  return jsonify([addr.to_json() for addr in addrs]), 200

def get_by_id(id):
  addr = Usuarios.query.get(id)
  if addr is None:
    return {"error": "Not found"}, 404
  return jsonify(addr.to_json())

def insert():
  if request.is_json:
    body = request.get_json()
    addr = Usuarios (
      nome = body["nome"],
      cpf = body["cpf"],
      email = body["email"],
      data = body["data"]    
    )
    
    db.session.add(addr)
    db.session.commit()
    return "Usuário Cadastrado.", 201
  return {"error": "Request must be JSON"}, 415


def update(id):
  if request.is_json:
    body = request.get_json()
    addr = Usuarios.query.get(id)
    if addr is None:
      return {"error": "Not found"}, 404
    if("nome" in body):
      addr.nome = body["nome"]
    if("cpf" in body):
      addr.cpf = body["cpf"]
    if("email" in body):
      addr.email = body["email"]
    if("data" in body):
      addr.data = body["data"]
  
    db.session.add(addr)
    db.session.commit()
    return "updated successfully", 200
  return {"error": "Request must be JSON"}, 415

def soft_delete(id):
  addr = Usuarios.query.get(id)
  if addr is None:
      return {"error": "Not found"}, 404
  addr.active = False   
  db.session.add(addr)
  db.session.commit()
  return "deleted successfully", 200
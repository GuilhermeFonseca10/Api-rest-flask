from config import db
from .tabelas.Lojas import Lojas
from .tabelas import Produtos
from flask import jsonify, request

def get_all():
  produtos = Produtos.query.all()
  return jsonify([produto.to_json() for produto in produtos]), 200

def get_by_id(id):
  produto = Produtos.query.get(id)
  if produto is None:
    return {"error": "Not found"}, 404
  return jsonify(produto.to_json())

def insert():
  if request.is_json:
    body = request.get_json()
    produto =  Produtos(
      nome = body["nome"],
      valor = body["valor"],
      quantidade = body["quantidade"],
      descricao = body["descricao"],
      lojas_id = body["lojas_id"]  
    )
    
    db.session.add(produto)
    db.session.commit()
    return "Produto Cadastrado.", 201
  return {"Erro": "A solicitação deve ser JSON"}, 415


def update(id):
  if request.is_json:
    body = request.get_json()
    produto = Produtos.query.get(id)
    if produto is None:
      return {"error": "Not found"}, 404
    if("nome" in body):
      produto.nome = body["nome"]
    if("valor" in body):
      produto.valor = body["valor"]
    if("quantidade" in body):
      produto.quantidade = body["quantidade"]
    if("descricao" in body):
      produto.descricao = body["descricao"]
    if("usuarios_id" in body):
        produto.lojas_id = body["lojas_id"]
    db.session.add(produto)
    db.session.commit()
    return "Atualizado com sucesso", 200
  return {"Erro": "A solicitação deve ser JSON"}, 415

def soft_delete(id):
  produto = Produtos.query.get(id)
  if produto is None:
      return {"error": "Not found"}, 404
  produto.active = False   
  db.session.add(produto)
  db.session.commit()
  return "Deletado com sucesso", 200
from config import db

class Produtos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    valor = db.Column(db.Numeric(10,2))
    quantidade = db.Column(db.Integer)
    descricao = db.Column(db.String(100))
    lojas_id = db.Column(db.Integer, db.ForeignKey("lojas.id"))

    def to_json(self):
       return {
        "id": self.id,
        "nome": self.nome,
        "valor": self.valor,
        "quantidade": self.quantidade,
        "descricao": self.descricao,
        "lojas_id": self.lojas_id
    }
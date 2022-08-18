from config import db

class Produtos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imagem = db.Column(db.String(100000),nullable=True)
    nome = db.Column(db.String(50),nullable=True)
    valor = db.Column(db.Numeric(10,2),nullable=True)
    quantidade = db.Column(db.Integer,nullable=True)
    descricao = db.Column(db.String(100),nullable=True)
    lojas_id = db.Column(db.Integer, db.ForeignKey("lojas.id"), nullable=True)

    def to_json(self):
       return {
        "id": self.id,
        "imagem": self.id,
        "nome": self.nome,
        "valor": self.valor,
        "quantidade": self.quantidade,
        "descricao": self.descricao,
        "lojas_id": self.lojas_id
        
    }
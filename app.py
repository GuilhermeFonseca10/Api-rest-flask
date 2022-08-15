from config import app
from flask_cors import CORS
from models.tabelas.Lojas import Lojas
from routes import Lojas, Produtos



cors = CORS(app)

if __name__ == '__main__':

  app.register_blueprint(Lojas.app)
  app.register_blueprint(Produtos.app)
  app.run(debug=True, host="0.0.0.0", port=8090)
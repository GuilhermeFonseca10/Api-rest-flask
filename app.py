from config import app
from flask_cors import CORS
from models.entities.Usuarios import Usuarios
from routes import Usuarios

cors = CORS(app)

if __name__ == '__main__':

  app.register_blueprint(Usuarios.app)
  app.run(debug=True, host="0.0.0.0", port=8090)
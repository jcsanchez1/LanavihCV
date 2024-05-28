from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_session import Session
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    """
    Función de fábrica que crea y configura una instancia de la aplicación Flask.
    """
    app = Flask(__name__)
   # Configuración de la aplicación
    app.config['SECRET_KEY'] = 'your_secret_key'  # Clave secreta para sesiones y seguridad
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/dblanavih'  # URI de la base de datos
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desactiva la funcionalidad de seguimiento de modificaciones  
    app.config['SESSION_TYPE'] = 'filesystem'

    # Inicializa SQLAlchemy con la aplicación
    db.init_app(app)

    # Configura CORS (Cross-Origin Resource Sharing)
    CORS(app, supports_credentials=True)

 # Contexto de la aplicación
    with app.app_context():
        # Importa los modelos para que se registren con SQLAlchemy
        from .models import Usuario, Rol, Modulo, RolModulo, Auditoria

        # Importa y registra las rutas
        from .routes import main_bp
        app.register_blueprint(main_bp)

    return app

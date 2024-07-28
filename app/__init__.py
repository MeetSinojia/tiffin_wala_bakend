from flask import Flask
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Change this to a strong key
    jwt = JWTManager(app)

    from app.blueprints.user_blueprint import user_bp
    app.register_blueprint(user_bp, url_prefix='/users')

    return app

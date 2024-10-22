import os
from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from .main import rota
from .routs import users, admin, norm_user
from .models import db



def config():
    app = Flask(__name__)

    UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'uploads')

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['SECRET_KEY'] = 'secret'
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY') or 'secreto'
    app.config['JWT_COOKIE_CSRF_PROTECT'] = False
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']


    db.init_app(app)
    Migrate(app, db)
    jwt = JWTManager(app)

    app.register_blueprint(rota)
    app.register_blueprint(users.rota_user)
    app.register_blueprint(admin.rota_admin)
    app.register_blueprint(norm_user.rota_user)
    
    return app



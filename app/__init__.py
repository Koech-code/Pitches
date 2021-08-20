from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_mail import Mail

mail=Mail()
db = SQLAlchemy()
login_manager = LoginManager()
bootstrap= Bootstrap()
login_manager.login_view='auth.login'
login_manager.session_protection='strong'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])

    # Initializing extensions 
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)


     # Registering the blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app


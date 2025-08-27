from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

db = SQLAlchemy()
login_manager = LoginManager()
DB_NAME = 'task.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Chab3456!@#'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        create_database()

    return app

def create_database():
    if not path.exists('website/' + DB_NAME):
        db.create_all()
        print('Database created Sucessfully!!')
    else:
        print('Database already exists')


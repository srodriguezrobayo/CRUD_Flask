from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

def create_app(config_name):
    app = Flask(__name__)
    user='root'
    passw=''
    url='localhost'
    name='proyecto'
    full_url=f'mysql://{user}:{passw}@{url}/{name}'
    app.config['SQLALCHEMY_DATABASE_URI'] = full_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app
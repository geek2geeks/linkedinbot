# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
db = SQLAlchemy(app)

from app import routes, models

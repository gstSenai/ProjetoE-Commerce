from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///mercado.db"
app.config["SECRET_KEY"] = 'c82f958a88d455d992956459'
db.init_app(app)

from mercado import routes
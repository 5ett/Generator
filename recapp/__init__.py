from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

load_dotenv()

replace_key = os.getenv('HIMITSU_BANGO')

app = Flask(__name__)
app.config['SECRET_KEY'] = replace_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///receipts.db'


db = SQLAlchemy(app)
crypt = Bcrypt(app)
daimyou = LoginManager(app)

from recapp import routes

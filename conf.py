import os
from datetime import timedelta
from distutils.util import strtobool
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

load_dotenv()
app = Flask(__name__)
# Test Co
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

#  Config pour la vrai BDD
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['ENV'] = os.getenv('ENV')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = bool(strtobool(os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')))
#
# CORS(app)
#db = SQLAlchemy(app)

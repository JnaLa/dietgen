from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/dietgen_db'
    JWT_SECRET_KEY = "sala"
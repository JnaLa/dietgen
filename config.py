import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST = 'localhost'
    DB_NAME = 'dietgen_db'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/dietgen_db'
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
    JWT_SECRET_KEY = "sala"

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Check SQLAlchemy URI
print(f"SQLALCHEMY_DATABASE_URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
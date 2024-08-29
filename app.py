from flask import Flask
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)
app.config.from_object('config.Config')
jwt = JWTManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


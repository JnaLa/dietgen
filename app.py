from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

app = Flask(__name__)
CORS(app)

# Configurations
app.config.from_object('config.Config')

# Initialize extensions
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import models after initializing SQLAlchemy
from models.users import User
from models.profiles import Profile

# Register blueprints
from routes import bp_foods, bp_users
app.register_blueprint(bp_foods)
app.register_blueprint(bp_users)

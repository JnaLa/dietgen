from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from sqlalchemy import text  # Import the text function

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
from routes import bp_foods, bp_users, bp_profiles
app.register_blueprint(bp_foods)
app.register_blueprint(bp_users)
app.register_blueprint(bp_profiles)

@app.route('/db_test', methods=['GET'])
def db_test():
    try:
        # Attempt to execute a simple query
        result = db.session.execute(text('SELECT 1'))
        return jsonify({"status": "success", "message": "Database is online"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
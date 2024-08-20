from app import db, bcrypt
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(500), unique=True, nullable=True)
    username = db.Column(db.String(100), unique=True, nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=True)
    password = db.Column(db.String(500), nullable=True)
    is_admin = db.Column(db.Boolean, default=False)
    
    def __init__(self, username, email, password, is_admin=False):
        self.public_id = str(uuid4())
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.is_admin = is_admin

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
        
    def obj_to_dict(self):
        return {
            "id": self.public_id,
            "username": self.username,
            "email": self.email,
            "is_admin": self.is_admin
        }
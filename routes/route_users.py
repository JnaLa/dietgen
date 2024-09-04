from flask import Blueprint, jsonify, request
from app import db
from models import User 
import logging

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

bp_users = Blueprint('bp_users', __name__)


@bp_users.route('/users/create', methods=['POST'])
def create_user():
    req = request.get_json(silent=True)
    if not req:
        return jsonify({'message': 'No valid JSON data within request'}), 400
    
    try:
        user = User(**req)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201

    except Exception as error:
        logging.error(f"Error creating user: {error}")
        return jsonify({'message': 'Failed to create user'}), 400
    

@bp_users.route('/users/login', methods=['POST'])
def login_user():
    login_data = request.get_json(silent=True)
    if not login_data:
        return jsonify({'message': 'No valid login data within request'}), 400
    
    try:
        user = User.query.filter_by(email=login_data.get('email')).first()

        if user and user.check_password(login_data.get('password')):
            access_token = create_access_token(identity=user.username)
            return jsonify({
                "access_token": access_token,
                'expiresIn': 1800,
                'is_admin': user.is_admin or False,
                'user_public_id' : user.public_id
                }), 200
        
        return jsonify({"message": "Invalid email or password"}), 401
        
    except Exception as error:
        logging.error(f"Error logging user: {error}")
        return jsonify({
            "message": 'Failed to login user'
        }), 400


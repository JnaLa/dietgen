from flask import Blueprint, jsonify, request
from app import db
from models import Profile
import logging

bp_profiles = Blueprint('bp_profiles', __name__)

@bp_profiles.route('/profiles/create', methods=['POST'])
def createProfile():
    req = request.get_json(silent=True)
    
    if not req:
        return jsonify({'message': 'No valid JSON data within request'}), 400
    
    try:
        profile = Profile(**req)
        db.session.add(profile)
        db.session.commit()
        return jsonify({'message': 'Profile created successfully'}), 201

    except Exception as error:
        logging.error(f"Error creating user: {error}")
        return jsonify({'message': 'Failed to create profile'}), 400

    
from flask import Blueprint, jsonify, request
from app import db
from models import Profile, User
import logging

bp_profiles = Blueprint('bp_profiles', __name__)

@bp_profiles.route('/profiles/create', methods=['POST'])
def createProfile():
    req = request.get_json(silent=True)
    
    if not req:
        return jsonify({'message': 'No valid JSON data within request'}), 400
    
    try:
        user = User.query.filter_by(public_id=req['user_public_id']).first()
        user_id = user.id

        new_profile = Profile(
            nickname = req['nickname'],
            age = req['age'],
            gender = req['gender'],
            height = req['height'],
            weight = req['weight'],
            bio = req['bio'],
            user_id = user_id
        )
        db.session.add(new_profile)
        db.session.commit()
        return jsonify({'message': 'Profile created successfully'}), 201

    except Exception as error:
        logging.error(f"Error creating profile: {error}")
        return jsonify({'message': 'Failed to create profile'}), 400
    

@bp_profiles.route('/user/profile/get/<string:user_public_id>', methods=['GET'])
def getUserProfile(user_public_id):
    # Fetch the user based on public_id
    profileUser = User.query.filter_by(public_id=user_public_id).first()

    if not profileUser:
        return jsonify({'message': 'User for profile not found'}), 404

    # Fetch the profile associated with the user
    profile = Profile.query.filter_by(user_id=profileUser.id).first()

    if not profile:
        return jsonify({'message': 'Profile not found'}), 404

    # Convert the profile to a dictionary and return it as JSON
    return jsonify(profile.obj_to_dict()), 200

    
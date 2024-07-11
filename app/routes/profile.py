from flask import Blueprint, Flask, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import User
from app.extensions import db, csrf
from flask_cors import CORS
from flask_cors import cross_origin

app = Flask(__name__)
CORS(app)
profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/', methods=['GET'])
@cross_origin()
@csrf.exempt
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if user:
        return jsonify({
            'full_name': user.full_name,
            'email': user.email,
            'password': user.password
        }), 200
    else:
        return jsonify({'error': 'User not found'}), 404

@profile_bp.route('/update', methods=['PUT'])
@cross_origin()
@csrf.exempt
@jwt_required()
def update_profile():
    user_id = get_jwt_identity()
    data = request.get_json()
    full_name = data.get('full_name')
    email = data.get('email')

    if not all([full_name, email]):
        return jsonify({'error': 'Full name and email are required'}), 400

    user = User.query.get(user_id)
    if user:
        user.full_name = full_name
        user.email = email
        db.session.commit()
        return jsonify({'message': 'Profile updated successfully'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404

@profile_bp.route('/change-password', methods=['PUT'])
@cross_origin()
@csrf.exempt
@jwt_required()
def change_password():
    user_id = get_jwt_identity()
    data = request.get_json()
    new_password = data.get('new_password')
    confirm_password = data.get('confirm_password')  # Fetch confirm_password from request data

    # Check if new_password and confirm_password are provided
    if not all([new_password, confirm_password]):
        return jsonify({'error': 'New password and confirm password are required'}), 400

    # Check if new_password matches confirm_password
    if new_password != confirm_password:
        return jsonify({'error': 'New password and confirm password must match'}), 400

    user = User.query.get(user_id)
    if user:
        # Set the new password for the user
        user.set_password(new_password)
        db.session.commit()
        return jsonify({'message': 'Password changed successfully'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404

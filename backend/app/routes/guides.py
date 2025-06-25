from flask import Blueprint, jsonify
from app.utils.firebase_init import db  # uses the initialized Firestore client

guides_bp = Blueprint('guides', __name__)

@guides_bp.route('/guides', methods=['GET'])
def get_guides():
    """
    Fetch all guides from Firestore collection "guides".
    Expects you have a Firestore collection named "guides".
    """
    try:
        guides_ref = db.collection("guides").stream()
        guides_list = []
        for doc in guides_ref:
            data = doc.to_dict()
            data['id'] = doc.id
            guides_list.append(data)
        return jsonify(guides_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

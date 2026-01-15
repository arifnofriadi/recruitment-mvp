from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from .models import Candidate, Client
from . import db
api_bp = Blueprint('api', __name__, url_prefix='/api')

# --- API Endpoints ---

@api_bp.route('/candidates', methods=['GET'])
def get_candidates():
    candidates = Candidate.query.all()
    return jsonify([candidate.to_dict() for candidate in candidates])

@api_bp.route('/candidates/<int:candidate_id>', methods=['GET'])
def get_candidate(candidate_id):
    candidate = Candidate.query.get(candidate_id)
    if not candidate:
        return jsonify({"error": "Candidate not found"}), 404
    return jsonify(candidate.to_dict())


@api_bp.route('/candidates', methods=['POST'])
def create_candidate():
    data = request.get_json() or {}
    required = ('name', 'email', 'role', 'internal_score')
    if not all(k in data for k in required):
        return jsonify({"error": "Missing required fields"}), 400

    candidate = Candidate(
        name=data.get('name'),
        email=data.get('email'),
        role=data.get('role'),
        internal_score=data.get('internal_score'),
        client_feedback=data.get('client_feedback')
    )
    db.session.add(candidate)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Email must be unique"}), 400

    return jsonify(candidate.to_dict()), 201


@api_bp.route('/candidates/<int:candidate_id>', methods=['PUT', 'PATCH'])
def update_candidate(candidate_id):
    candidate = Candidate.query.get(candidate_id)
    if not candidate:
        return jsonify({"error": "Candidate not found"}), 404

    data = request.get_json() or {}
    # allow partial updates
    for field in ('name', 'email', 'role', 'internal_score', 'client_feedback'):
        if field in data:
            setattr(candidate, field, data.get(field))

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Email must be unique"}), 400

    return jsonify(candidate.to_dict())


@api_bp.route('/candidates/<int:candidate_id>', methods=['DELETE'])
def delete_candidate(candidate_id):
    candidate = Candidate.query.get(candidate_id)
    if not candidate:
        return jsonify({"error": "Candidate not found"}), 404

    db.session.delete(candidate)
    db.session.commit()
    return jsonify({"success": "Candidate deleted"}), 200

@api_bp.route('/clients', methods=['GET'])
def get_clients():
    clients = Client.query.all()
    return jsonify([client.to_dict() for client in clients])

@api_bp.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    client = Client.query.get(client_id)
    if not client:
        return jsonify({"error": "Client not found"}), 404
    return jsonify(client.to_dict())
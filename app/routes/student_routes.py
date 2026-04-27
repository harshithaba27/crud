from flask import Blueprint, request, jsonify
from app.services.supabase_service import supabase_service

student_bp = Blueprint('student', __name__)

@student_bp.route('/students', methods=['GET'])
def get_students():
    try:
        data = supabase_service.get_all()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@student_bp.route('/students', methods=['POST'])
def add_student():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400
        result = supabase_service.create(data)
        return jsonify({"message": "Student added", "data": result}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@student_bp.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400
        result = supabase_service.update(id, data)
        return jsonify({"message": "Updated", "data": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@student_bp.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    try:
        supabase_service.delete(id)
        return jsonify({"message": "Deleted"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

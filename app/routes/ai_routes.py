from flask import Blueprint, request, jsonify
from app.services.ollama_service import ollama_service
from app.services.supabase_service import supabase_service

ai_bp = Blueprint('ai', __name__)

@ai_bp.route('/ask', methods=['POST'])
def ask_ai():
    try:
        user_query = request.json.get('query')
        if not user_query:
            return jsonify({"error": "No query provided"}), 400

        # Fetch data for context
        students_data = supabase_service.get_all()
        
        # Call AI service
        answer = ollama_service.ask(user_query, students_data)
        
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

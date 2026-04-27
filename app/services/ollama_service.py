import requests
import json
from app.config import Config

class OllamaService:
    def __init__(self):
        self.url = Config.OLLAMA_URL
        self.model = Config.OLLAMA_MODEL

    def ask(self, query, context_data):
        context = json.dumps(context_data, indent=2)
        
        system_prompt = (
            "You are an AI assistant for a Student Management System. "
            "Below is the current list of students in the database:\n"
            f"{context}\n\n"
            "Rules:\n"
            "1. ONLY answer questions based on the provided student data.\n"
            "2. If a student is not in the list, say they don't exist.\n"
            "3. If the user asks about something unrelated to these students or the database, "
            "politely inform them that you only help with queries related to the student database.\n"
            "4. Be concise and professional.\n\n"
            f"User Question: {query}"
        )

        try:
            response = requests.post(
                self.url,
                json={
                    "model": self.model,
                    "prompt": system_prompt,
                    "stream": False
                },
                timeout=60
            )
            
            if response.status_code != 200:
                raise Exception(f"Ollama Error {response.status_code}: {response.text}")
                
            result = response.json()
            return result.get('response', 'No response from AI')
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"Ollama Connection Error: {str(e)}")
        except Exception as e:
            raise Exception(f"Ollama Service Error: {str(e)}")

ollama_service = OllamaService()

from supabase import create_client
from app.config import Config

class SupabaseService:
    def __init__(self):
        self.client = create_client(Config.SUPABASE_URL, Config.SUPABASE_KEY)
        self.table_name = 'students'

    def get_all(self):
        try:
            response = self.client.table(self.table_name).select("*").execute()
            return response.data
        except Exception as e:
            raise Exception(f"Supabase GET Error: {str(e)}")

    def create(self, data):
        try:
            response = self.client.table(self.table_name).insert(data).execute()
            return response.data
        except Exception as e:
            raise Exception(f"Supabase INSERT Error: {str(e)}")

    def update(self, id, data):
        try:
            response = self.client.table(self.table_name).update(data).eq('id', id).execute()
            return response.data
        except Exception as e:
            raise Exception(f"Supabase UPDATE Error: {str(e)}")

    def delete(self, id):
        try:
            response = self.client.table(self.table_name).delete().eq('id', id).execute()
            return response.data
        except Exception as e:
            raise Exception(f"Supabase DELETE Error: {str(e)}")

supabase_service = SupabaseService()

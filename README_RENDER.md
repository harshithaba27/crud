# Deployment on Render

This project is ready to be deployed on [Render](https://render.com/).

## Steps to Deploy:

1. **Create a new Web Service** on Render.
2. **Connect your GitHub repository**.
3. **Configure the build and start commands**:
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
4. **Add Environment Variables** in the Render Dashboard:
   - `SUPABASE_URL`: Your Supabase Project URL
   - `SUPABASE_KEY`: Your Supabase Anon Key
   - `OLLAMA_URL`: (Optional) URL to your Ollama instance (Note: Render's free tier might not be enough to run Ollama locally on the same instance; consider using a remote Ollama or a different AI provider if needed).
   - `OLLAMA_MODEL`: (Optional) Default is `llama3.2:1b`.
   - `SECRET_KEY`: A long random string for Flask session security.

## Local Development with venv

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate it:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   python app.py
   ```

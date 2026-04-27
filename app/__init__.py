from flask import Flask
from app.config import Config
from app.routes.student_routes import student_bp
from app.routes.ai_routes import ai_bp
from flask import render_template

def create_app():
    app = Flask(__name__, 
                static_folder='../static', 
                template_folder='../templates')
    app.config.from_object(Config)

    # Register Blueprints
    app.register_blueprint(student_bp)
    app.register_blueprint(ai_bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app

app = create_app()

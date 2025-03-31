from flask import Flask
from dotenv import load_dotenv
import os
from flask_cors import CORS

from app.routes.query_routes import query_bp

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Configurations
    app.config['GEMINI_API_KEY'] = os.getenv('GEMINI_API_KEY')

    # Register the query routes
    app.register_blueprint(query_bp, url_prefix="/api")

    @app.route('/health', methods=['GET'])
    def health():
        return {"status": "Running"}, 200

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

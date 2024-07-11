from flask import Flask
from app.config import Config
from app.routes import mpesa
from app.models import db

app = Flask(__name__)
app.config.from_object(Config)

# Initialize SQLAlchemy
db.init_app(app)

app.register_blueprint(mpesa)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
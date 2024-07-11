from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate = Migrate(app, db)

    # Import models to ensure they are registered with SQLAlchemy
    from .models import MpesaCalls, MpesaCallBacks, MpesaPayment  # Importing your models here

    with app.app_context():
        db.create_all()  # Create database tables

    return app

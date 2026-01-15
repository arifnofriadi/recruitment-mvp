from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import Config

db = SQLAlchemy()
cors = CORS()

def create_app():
    """Create and configure the app."""
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    cors.init_app(app)

    from .models import Candidate, Client
    # Register blueprint
    from . import routes
    app.register_blueprint(routes.api_bp)

    @app.cli.command("seed-db")
    def seed_db():
        """Add data to the database."""
        with app.app_context():
            db.create_all()
            # Remove old data
            Candidate.query.delete()
            Client.query.delete()
            db.session.commit()

            seed_candidates = [
                Candidate(name='Budi Santoso', email='budi@example.com', role='Backend Engineer', internal_score=85),
                Candidate(name='Siti Nurhaliza', email='siti@example.com', role='Data Scientist', internal_score=90),
                Candidate(name='Ahmad Fadli', email='ahmad@example.com', role='Frontend Engineer', internal_score=78, client_feedback="Kurang percaya diri saat menjelaskan proyek."),
                Candidate(name='Maya Anggraini', email='maya@example.com', role='Product Manager', internal_score=92)
            ]
            seed_clients = [
                Client(name='TechCorp Indonesia', industry='Fintech', requirements_summary='Mencari engineer dengan pengalaman microservices dan komunikasi yang baik.'),
                Client(name='StartupKu', industry='E-commerce', requirements_summary='Butuh frontend yang fast-learner dan bisa beradaptasi dengan startup environment yang dinamis.'),
                Client(name='DataMaju', industry='Data Analytics', requirements_summary='Membutuhkan data scientist yang mampu menyajikan insight bisnis dengan jelas.')
            ]
            db.session.bulk_save_objects(seed_candidates)
            db.session.bulk_save_objects(seed_clients)
            db.session.commit()
            print("Database seeded!")
    
    return app
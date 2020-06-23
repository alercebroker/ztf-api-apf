from flask import Flask
from api.ztf import ztf_api

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    ztf_api.init_app(app)

    with app.app_context():
        from .db import db, session_options
        db.connect(config=app.config["DATABASE"]["SQL"], session_options=session_options, use_scoped=True)
        def cleanup(e):
            db.session.remove()
            return e
        app.teardown_appcontext(cleanup)
    return app
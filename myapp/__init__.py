import os

from flask import Flask 

from .extensions import db
from .routes import main

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

#postgres://five_two_db_user:kkUsE52r2PnExnZrJvL3oUue9Tzq2jxT@dpg-cog0av8l5elc73dm3iq0-a.oregon-postgres.render.com/five_two_db

    db.init_app(app)

    app.register_blueprint(main)

    return app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import os


app = Flask(__name__)
app.config.from_object(os.environ.get('CONFIG') or 'config.DevelopmentConfig')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.views.main import main as main_blueprint
app.register_blueprint(main_blueprint)

from app import models

# Import routes and Models at bottom of file because they depend on creation of app
# importing them last prevents cirulcalar dependencies
# for larger applications app factory is recommended

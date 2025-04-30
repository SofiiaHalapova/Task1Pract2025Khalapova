from flask import Flask

from Task1Pract2025.website.views import views


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'key_pract_halapova_2025'

    app.register_blueprint(views, url_prefix='/')

    return app

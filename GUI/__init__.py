from flask import Flask
from kinepolis.Kinepolis import Kinepolis

kinepolis = Kinepolis()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hfasjklowrjewlqrrjalkvjocioasjdlk'
    
    from .views import views

    app.register_blueprint(views, url_prefix='/')
    return app

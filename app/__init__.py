from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.articles import bp as articles_bp
    app.register_blueprint(articles_bp)

    return app
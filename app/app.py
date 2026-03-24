from flask import Flask, app, render_template, redirect, url_for
from . import projects, simple_pages

def create_app() -> app:
    app: Flask = Flask(__name__)
    app.config.from_object('app.config')

    register_blueprints(app)

    return app
#Blueprints
def register_blueprints(app: Flask) -> None:
    app.register_blueprint(projects.routes.blueprint)
    app.register_blueprint(simple_pages.routes.blueprint)
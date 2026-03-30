from flask import Flask, app, render_template, redirect, url_for
from . import projects, simple_pages, admin
from app.extensions.database import db, migrate


def create_app() -> app:
    app: Flask = Flask(__name__)
    app.config.from_object('app.config')
    app.url_map.strict_slashes = False

    register_extension(app)
    register_blueprints(app)

    return app
#Blueprints
def register_blueprints(app: Flask) -> None:
    app.register_blueprint(projects.routes.blueprint)
    app.register_blueprint(simple_pages.routes.blueprint)
    app.register_blueprint(admin.routes.blueprint)

#load external tools (DB, APIs, ...)
def register_extension(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
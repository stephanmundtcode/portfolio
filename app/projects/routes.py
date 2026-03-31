# database
from sqlalchemy import select
from app.extensions.database import db

from .models import Project
from flask import Blueprint, render_template
import json

def load_json(file) -> list[dict] | str:
     try:
        with open(file, 'r') as f:
            data = json.load(f)
            return data
     except FileNotFoundError:
          return "Error: File not found!"

blueprint = Blueprint('projects', __name__)

@blueprint.get('/projects')
def projects() -> str:
    stmt = select(Project).order_by(Project.year)
    projects = db.session.scalars(stmt).all()
    return render_template('projects/index.html', projects=projects)


@blueprint.get('/projects/<slug>')
def project(slug) -> str:
    stmt = select(Project)
    projects = db.session.scalars(stmt).all()
    for project in projects:
        if slug == project.slug:
            return render_template('projects/single_project.html', project=project)
    
    return "Sorry, unfortunately there is no project like that :(", 404
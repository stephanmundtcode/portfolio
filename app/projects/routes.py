from .models import Project
from flask import Blueprint, render_template
import json

PROJECT_DATA_PATH: str = "app/mock_data/projects.json"

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
    projects = load_json(PROJECT_DATA_PATH)
    for project in projects:
        project["tags"] = " | ".join(project["tags"])

    return render_template('projects/index.html', projects=projects)


@blueprint.get('/projects/<slug>')
def project(slug) -> str:
    projects = load_json(PROJECT_DATA_PATH)
    for project in projects:
        if slug == project["slug"]:
            return render_template('projects/single_project.html', project=project)
    
    return "Sorry, unfortunately there is no project like that :(", 404
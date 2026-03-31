from sqlalchemy import select
from app.app import create_app
from app.projects.models import Project, Tag
from app.extensions.database import db

from app.projects.routes import load_json

PROJECT_DATA_PATH: str = "app/mock_data/projects.json"

if __name__ == '__main__':
    app = create_app()
    app.app_context().push()

    projects = load_json(PROJECT_DATA_PATH)

    for project in projects:

        new_project = Project(slug=project["slug"], title=project["title"], description=project["description"], link=project["link"], year=project["year"])
        db.session.add(new_project)

        for tag_name in project["tags"]:
            stmt =  select(Tag).where(Tag.tag == tag_name)
            result = db.session.execute(stmt).scalar()
            if result == None:
                new_tag = Tag(tag=tag_name)
                db.session.add(new_tag)
            else:
                new_tag = result
            
            new_project.tags.append(new_tag)

    db.session.commit()
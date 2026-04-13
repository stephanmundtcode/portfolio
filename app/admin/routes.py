from werkzeug.security import check_password_hash
from flask import Blueprint, render_template, request, url_for, redirect, session, flash
from dotenv import load_dotenv
from sqlalchemy import select
from app.extensions.database import db
from app.simple_pages.models import Contact
from app.projects.models import Project, Tag

import os

load_dotenv()

blueprint = Blueprint('admin', __name__)

def login_required():
    if not session.get("logged_in"):
        return redirect(url_for("admin.login"))

@blueprint.route("/login", methods=['GET', 'POST'])
def login() -> str:
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        admin_username = os.getenv("ADMIN_USERNAME")
        admin_password = os.getenv("ADMIN_PASSWORD")

        if username == admin_username and check_password_hash(admin_password, password):
            session["logged_in"] = True
            return redirect(url_for('admin.index'))
        else:
            return render_template('admin/login.html', error="Invalid username or password.")

    return render_template("admin/login.html")


@blueprint.get("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("admin.login"))

@blueprint.get("/admin")
def index():
    check = login_required()
    if check:
        return check

    stmt = select(Contact).order_by(Contact.created_at.desc())
    inquiries = db.session.scalars(stmt).all()

    return render_template("admin/index.html", inquiries=inquiries)

@blueprint.get("/admin/projects")
def projects():
    check = login_required()
    if check:
        return check

    stmt = select(Project).order_by(Project.year.desc())
    projects = db.session.scalars(stmt).all()

    return render_template("admin/projects.html", projects=projects)

@blueprint.post("/admin/projects/add")
def add_project():
    check = login_required()
    if check:
        return check

    new_project = Project(
        title=request.form.get("title"),
        slug=request.form.get("slug"),
        description=request.form.get("description"),
        link=request.form.get("link"),
        year=request.form.get("year"),
        picture_url=request.form.get("picture_url") or None
    )

    tag_string = request.form.get("tags", "")
    for tag_name in tag_string.split(","):
        tag_name = tag_name.strip()
        if tag_name:
            stmt = select(Tag).where(Tag.tag == tag_name)
            existing_tag = db.session.execute(stmt).scalar()
            if existing_tag is None:
                existing_tag = Tag(tag=tag_name)
                db.session.add(existing_tag)
            new_project.tags.append(existing_tag)

    db.session.add(new_project)
    db.session.commit()
    flash("Project added!")
    return redirect(url_for("admin.projects"))

@blueprint.post("/admin/projects/delete/<slug>")
def delete_project(slug):
    check = login_required()
    if check:
        return check

    stmt = select(Project).where(Project.slug == slug)
    project = db.session.execute(stmt).scalar()

    if project:
        db.session.delete(project)
        db.session.commit()
        flash("Project deleted!")

    return redirect(url_for("admin.projects"))

@blueprint.get("/admin/projects/edit/<slug>")
def edit_project(slug):
    check = login_required()
    if check:
        return check

    stmt = select(Project).where(Project.slug == slug)
    project = db.session.execute(stmt).scalar()

    if not project:
        flash("Project not found!")
        return redirect(url_for("admin.projects"))

    return render_template("admin/edit_project.html", project=project)

@blueprint.post("/admin/projects/edit/<slug>")
def update_project(slug):
    check = login_required()
    if check:
        return check

    stmt = select(Project).where(Project.slug == slug)
    project = db.session.execute(stmt).scalar()

    if not project:
        flash("Project not found!")
        return redirect(url_for("admin.projects"))

    project.title = request.form.get("title")
    project.slug = request.form.get("slug")
    project.description = request.form.get("description")
    project.link = request.form.get("link")
    project.year = request.form.get("year")
    project.picture_url = request.form.get("picture_url") or None

    project.tags.clear()
    tag_string = request.form.get("tags", "")
    for tag_name in tag_string.split(","):
        tag_name = tag_name.strip()
        if tag_name:
            stmt = select(Tag).where(Tag.tag == tag_name)
            existing_tag = db.session.execute(stmt).scalar()
            if existing_tag is None:
                existing_tag = Tag(tag=tag_name)
                db.session.add(existing_tag)
            project.tags.append(existing_tag)

    db.session.commit()
    flash("Project updated!")
    return redirect(url_for("admin.projects"))

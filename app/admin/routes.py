from werkzeug.security import check_password_hash
from flask import Blueprint, render_template, request, url_for, redirect, session
from dotenv import load_dotenv
from sqlalchemy import select
from app.extensions.database import db
from app.simple_pages.models import Contact
from app.projects.models import Project

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





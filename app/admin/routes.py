from flask import Blueprint, render_template

blueprint = Blueprint('admin', __name__)

@blueprint.get("/admin")
def admin() -> str:
    return render_template("admin/index.html")
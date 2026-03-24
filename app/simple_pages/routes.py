from flask import Blueprint, render_template, redirect, url_for

blueprint = Blueprint('simple_pages', __name__)

@blueprint.get('/')
def index() -> str:
    return render_template('simple_pages/index.html')

@blueprint.get('/index')
def index_redirect():
    return redirect(url_for('simple_pages.index'))

@blueprint.get('/contact')
def contact() -> str:
        return render_template('simple_pages/contact.html')
from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for, request
from app.extensions.database import db
from app.simple_pages.models import Contact


blueprint = Blueprint('simple_pages', __name__)

@blueprint.get('/')
def index() -> str:
    return render_template('simple_pages/index.html')

@blueprint.get('/index')
def index_redirect() -> str:
    return redirect(url_for('simple_pages.index'))

@blueprint.route('/contact' , methods=['GET', 'POST'])
def contact() -> str:
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        date = datetime.utcnow()

        new_entry = Contact(name=name, email=email, message=message, created_at=date)
        db.session.add(new_entry)
        db.session.commit()
        
    return render_template('simple_pages/contact.html')
# Portfolio

My personal portfolio website. Built with Flask as a learning project, completely without AI.

Deployed on [Render](https://render.com).

## What it does

- Shows my projects with tags, descriptions and links
- Contact form that stores messages in the database
- Small word typing game after submitting the contact form
- Admin panel to manage projects (add, edit, delete) and view contact inquiries

## Tech Stack

- Python / Flask
- SQLAlchemy + Flask-Migrate
- Jinja2 Templates
- PostgreSQL
- Gunicorn (production)

## Setup

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```
FLASK_APP=run.py
FLASK_DEBUG=True
DATABASE_URL=<your database url>
SECRET_KEY=<your secret key>
ADMIN_USERNAME=<your admin username>
ADMIN_PASSWORD=<your admin password>
```

## Database

```bash
flask db upgrade
flask seed
```

`flask seed` loads initial project data from `app/mock_data/projects.json`.

## Run

Development:

```bash
python run.py
```

Production:

```bash
gunicorn wsgi:app
```

---

**Production Link:** https://portfolio-bm3c.onrender.com/

**Admin Panel:** https://portfolio-bm3c.onrender.com/admin

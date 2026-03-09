from flask import Flask, render_template, redirect, url_for
import json

PROJECT_DATA_PATH = "mock_data/projects.json"

def load_json(file) -> list[dict] | str:
     try:
        with open(file, 'r') as f:
            data = json.load(f)
            return data
     except FileNotFoundError:
          return "Error: File not found!"
          

app: Flask = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def index() -> str:
    return render_template('index.html')

@app.route('/index')
def index_2():
    return redirect(url_for('index'))

@app.route('/projects')
def projects() -> str:
    projects = load_json(PROJECT_DATA_PATH)
    for project in projects:
        project["tags"] = " | ".join(project["tags"])
        print(project["tags"])

    return render_template('projects.html', projects=projects)

'''@app.route('/projects/<slug>')
def project(slug) -> str:
    projects = load_json(PROJECT_DATA_PATH)
    for project in projects:
        if slug == project["slug"]:
            return project
    
    return("The Project you are looking for is not available :(")
'''

@app.route('/contact')
def contact() -> str:
        return render_template('contact.html')

if __name__ == '__main__':
    app.run(port=8000)

# Website: https://codecookies.xyz/flask-tutorial/v1/templating-with-jinja
# Current Progress: Jinja: loop (and conditions)
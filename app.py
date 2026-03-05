from flask import Flask, redirect, url_for


app: Flask = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def index() -> str:
    return 'My name is Jeff'

@app.route('/about')
def about() -> str:
    return 'I like cookies'

@app.route('/about-me')
def about_me() -> Flask:
    return redirect(url_for('about'))

@app.route('/double/<num>')
def double(num: str) -> str:
        return str(int(num)*2)

if __name__ == '__main__':
    app.run()

# Website: https://codecookies.xyz/flask-tutorial/v1/routing
# Current Progress: HTTP methods
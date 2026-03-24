from app.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(port=8000)


# Website: https://codecookies.xyz/flask-tutorial/v1/unit-testing#testing-page-content
# Current Progress: Jinja: Testing
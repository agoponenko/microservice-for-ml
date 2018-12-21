from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print('hi')
    return '<h1>Hello, my good friend!</h1>'
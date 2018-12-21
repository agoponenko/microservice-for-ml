from flask import Flask, request, jsonify
import numpy as np
from sklearn.externals import joblib 

app = Flask(__name__)
knn = joblib.load('knn.jbl')

@app.route('/')
def hello_world():
    print('hi')
    return '<h1>Hello, my good friend!</h1>'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    username = float(username) * float(username)
    return 'User %s' % username

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

@app.route('/avg/<nums>')
def avg(nums):
    nums = nums.split(',')
    nums = [float(num) for num in nums]
    nums_mean = mean(nums)
    print(nums_mean)
    return str(nums_mean)

@app.route('/iris/<params>')
def iris(params):
    params = params.split(',')
    params = [float(param) for param in params]
    params = np.array(params).reshape(1,-1)
    predictions = knn.predict(params)
    return str(predictions)

@app.route('/show_image')
def show_image():
    return  '<img src="/static/setosa.jpg" alt="setosa">' # works only on /static wtf?


@app.route('/iris_post', methods=['GET', 'POST'])
def add_message():
    content = request.get_json()
    params = content['flower'].split(',')
    params = [float(param) for param in params]
    params = np.array(params).reshape(1,-1)
    predictions = knn.predict(params)
    predictions = {'class':str(predictions[0])}
    return jsonify(predictions)
from flask import Flask
app = Flask(__name__)

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

    print(params)

    import numpy as np
    from sklearn import datasets
    iris = datasets.load_iris()
    iris_X = iris.data
    iris_y = iris.target

    np.random.seed(0)
    indices = np.random.permutation(len(iris_X))
    iris_X_train = iris_X[indices[:-10]]
    iris_y_train = iris_y[indices[:-10]]
    iris_X_test = iris_X[indices[-10:]]
    iris_y_test = iris_y[indices[-10:]]

    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier()
    knn.fit(iris_X_train, iris_y_train) 
    KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
            metric_params=None, n_jobs=None, n_neighbors=5, p=2,
            weights='uniform')

    params = np.array(params).reshape(1,-1)

    predictions = knn.predict(params)
    
    return str(predictions)
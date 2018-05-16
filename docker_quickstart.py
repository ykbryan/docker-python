from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized. Hello World! 2!'

@app.route('/flaskfargatedemo')
def hello_fargate():
    return 'Hello Fargate!'

@app.route('/api')
def hello_fargate():
    return 'Hello API Endpoint!'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

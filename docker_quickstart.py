from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized. Hello World! 3!'

@app.route('/flaskfargatedemo')
def hello_fargate():
    return 'Hell Fargate!'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

from flask import Flask
app = Flask(__name__) #__name__ is same as hello.py

#create endpoints
@app.route('/') #decorators
def hello_world():
    #this function will automatically execute
    return '<h1> Hello World!! </h1>'

@app.route('/ping')
def ping():
    return {'message' : 'why are you pinging me?'}
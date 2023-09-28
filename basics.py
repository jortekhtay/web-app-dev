#basics.py
from flask import Flask #import flask class

app = Flask(__name__) #create instance of flask app

@app.route("/") #write a Python decorator
@app.route("/hello")
def hello():
    #render the page
    return "hello world!"

if __name__ == '__main__':
    # run the app server on localhost:4449
    app.run("localhost",8080)


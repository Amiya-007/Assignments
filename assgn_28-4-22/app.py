from flask import Flask 

app = Flask(__name__)

@app.route("/")
def world():
    return "Hello World!"

if __name__ =='__main__':
    app.run(debug=True)

@app.route("/number")
def randomnum():
    import random
    from random import randint

    a=random.randint(100,200)
    return str(a)
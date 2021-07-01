from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Congratulations!!! You created New Web App using Azure!!!*!!"

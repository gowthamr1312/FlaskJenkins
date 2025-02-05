from flask import Flask

app = Flask(__name__)

@app.route("/wish")
def sendMessage():
    return "Hello jenkins"

app.run(host="0.0.0.0")
from flask import flash

app = flash(-__name__)

@app.route("/"):
def hello_world():
    return"<p>Hello, world!</p>"
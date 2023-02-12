from flask import Flask
from flask import render_template

from app.asset import Asset

app = Flask(__name__)
Asset(app)

@app.route("/")
def index():
    return render_template("main.html")


if __name__ == '__main__':
    app.run()

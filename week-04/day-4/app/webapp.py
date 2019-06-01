from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="SNA")

@app.route("/mentions/")
def mentions():
    return render_template("mentions.html")

@app.route("/reactions/")
def reactions():
    return render_template("reactions.html")


if __name__ == "__main__":
    app.run(port=5001, debug=True)
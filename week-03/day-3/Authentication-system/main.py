from flask import Flask, render_template
from form import LoginForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)


@app.route("/")
def login():
    form = LoginForm()
    return render_template("login.html", form=form)
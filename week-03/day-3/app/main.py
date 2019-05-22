from flask import Flask, render_template
from form import NameForm, PriceForm, QTYForm
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'


### HTML Workshop
@app.route("/firstweb")
def firstweb():
    return render_template("first-web.html")


### Movies
movies = {
    1: "The Silence of the Lambs",
    2: "Whiplash",
    3: "Good Will Hunting",
    4: "El secreto de sus ojos"
    }

@app.route("/")
def index():
    return render_template("index.html", movies=movies)

@app.route("/<int:movie_id>")
def movie(movie_id):
    with open(f"./movie_database/{movie_id}.txt", "r") as f:
        year = f.readline()
        director = f.readline()
        stars = f.readline()
    return render_template("movie.html", title=movies[movie_id], 
                            year=year, director=director, stars=stars)


##### Web Form
def queryProducts(data):
    with open("products") as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        


@app.route("/webform", methods=['GET', 'POST'])
def webform():
    name = None
    price = None
    qty = None
    form1 = NameForm()
    form2 = PriceForm()
    form3 = QTYForm()
    if form1.validate_on_submit():
        name = form1.name.data
        form1.name.data = ""
    if form2.validate_on_submit():
        price = form2.price.data
        form2.price.data = ""
    if form3.validate_on_submit():
        qty = form3.qty.data
        form3.qty.data = ""

    return render_template("webform.html", 
                            nameform=form1, priceform=form2, qtyform=form3,
                            name=name, price=price, qty=qty)


if __name__ == "__main__":
    app.run(debug=True)
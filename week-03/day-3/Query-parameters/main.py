from flask import Flask, render_template, redirect, url_for
from form import ProductForm



app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

@app.route("/", methods=['GET', 'POST'])
def webform():
    data = None
    form = ProductForm()
    if form.validate_on_submit():
        if form.name.data:
            data = form.name.data
        elif form.price.data:
            data = form.price.data
        else:
            data = form.qty.data
        return redirect(url_for("productinfo"))
    return render_template("webform.html", form=form)


def queryProducts(data):
    with open("products.csv") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        for row in reader:
            pass


@app.route("/productinfo")
def productinfo():
    return "abc"



if __name__ == "__main__":
    app.run(debug=True)
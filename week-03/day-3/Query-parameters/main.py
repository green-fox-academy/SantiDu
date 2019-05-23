from flask import Flask, render_template, request, redirect, url_for, session
from form import ProductForm
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

@app.route("/", methods=['GET', 'POST'])
def webform():
    data = None
    field = None
    form = ProductForm()
    if form.validate_on_submit():
        if form.name.data:
            data = request.form.get("field")
            field = "name"
        elif form.price.data:
            data = request.form.get('field')
            field = "price"
        else:
            data = request.form.get('field')
            field = "qty"
        session["data"] = queryProducts(data, field)
        return redirect(url_for("productinfo"))
    return render_template("webform.html", form=form)


def queryProducts(data, field):
    with open("./static/products.csv") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        output = []
        for row in reader:
            if field in ["qty", "price"]:
                if row[field] == data:
                    output.append(row)
            else:
                if data in row[field]:
                    output.append(row)
        return output


@app.route("/productinfo")
def productinfo():
    output = session["data"]
    return f"{output}"



if __name__ == "__main__":
    app.run(debug=True)
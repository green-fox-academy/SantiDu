from flask import Flask, render_template, flash, session, redirect, url_for
from form import HouseForm
from postcodes import df
import pickle
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'blablalala - hard to guess string'
Bootstrap(app)

with open("linear_regression.pkl", "rb") as pfile:
    model = pickle.load(pfile)

def get_lat_lon(postcode):
    lat_lon = df[df["postcode"] == postcode.upper()]
    return [lat_lon.latitude.values[0], lat_lon.longitude.values[0]]


def pt_back(pt):
    pts = ['D', 'F', 'S', 'T']
    return [0] * pts.index(pt) + [1] + (3 - pts.index(pt)) * [0]


def to_predict_list(form):
    return [[form.bedroomnumber.data, form.duration.data, form.old_new.data] + 
    get_lat_lon(form.postcode.data) + pt_back(form.propertytype.data)]


def ValuePredictor(to_predict_list):
    result = model.predict(to_predict_list)
    return result[0]


@app.route("/", methods=['GET', 'POST'])
def index():
    form = HouseForm()
    predicted_v = ""
    if form.validate_on_submit():
        predicted_v = '£' + '{:20,.2f}'.format(round(ValuePredictor(to_predict_list(form)), 2))
        session["value"] = predicted_v
        return redirect(url_for("predicted"))
    elif form.errors:
        for errors in form.errors.values():
            for error in errors:
                flash(f"{error}", category='error')
    return render_template("index.html", form=form)

@app.route("/predicted")
def predicted():
    return render_template("predicted.html", predicted=session["value"])

if __name__ == "__main__":
    app.run(debug=True)

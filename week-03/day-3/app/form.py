from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField


class NameForm(FlaskForm):
    name = StringField("Search by name")
    submit = SubmitField("Search")

class PriceForm(FlaskForm):
    price = IntegerField("Search by price")
    submit = SubmitField("Search")

class QTYForm(FlaskForm):
    qty = IntegerField("Search by quantity")
    submit = SubmitField("Search")
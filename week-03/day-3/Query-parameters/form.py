from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    field = StringField("What product do you want?", validators=[DataRequired()])
    name = SubmitField("Search by name")
    price = SubmitField("Search by price")
    qty = SubmitField("Search by quantity")
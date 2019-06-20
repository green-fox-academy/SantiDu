from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import InputRequired, DataRequired, AnyOf, NumberRange
from postcodes import df

class HouseForm(FlaskForm):
    bedroomnumber = IntegerField('Bedroom Number', [DataRequired(message="Please provide a valid bedroom number"), 
                                                    NumberRange(0, message="The bedroom number must be at least 0.")])
    postcode = StringField("Postcode", [InputRequired(), 
                                        AnyOf(df["postcode"].to_list(), message="Please provide a valid postcode.")])
    propertytype = SelectField("Property Type", coerce=str, choices=[("D", 'Detached'), 
                                                        ("S", 'Semi-Detached'), 
                                                        ("T", 'Terraced'),
                                                        ("F", 'Flats/Maisonettes')])
    old_new = SelectField("Old/New", coerce=int, choices=[(0, 'Old'), (1, 'New')])
    duration = SelectField('Duration', coerce=int, choices=[(1, 'Freehold'), (0, 'Leasehold')])
    submit = SubmitField("Submit")
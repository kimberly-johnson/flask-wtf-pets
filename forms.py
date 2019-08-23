from flask_wtf import FlaskForm
from wtforms import StringField, Floatfield, IntegerField, BooleanField

class AddPetForm(FlaskForm):
    """Form for adding pet."""
    name = StringField("Pet Name")
    species = StringField("Species")
    photo_url = StringField("Photo URL")
    age = IntegerField("Age")
    notes = StringField("Notes")
    available = BooleanField("Availability")
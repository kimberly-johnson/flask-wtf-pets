from flask import Flask, render_template, request, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']
debug = DebugToolbarExtension(app)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route("/")
def display_homepage():
    """display list of pets"""

    pets = Pet.query.all()

    return render_template("index.html", pets=pets)
    
@app.route("/add", methods=["POST, GET"])
def add_pet():
    """display, handle add pet form"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data 
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        return redirect("/")

    else:
        return render_template("", form=form)
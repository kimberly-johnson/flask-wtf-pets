"""models for pet_adoption"""
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Class for pet instance."""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text, 
                     nullable=False)
    species = db.Column(db.Text, 
                        nullable=False)
    photo_url = db.Column(db.Text,
                          nullable=True, 
                          default="https://www.tourniagara.com/wp-content/uploads/2014/10/default-img.gif")
    age = db.Column(db.Integer,
                    nullable=False)
    notes = db.Column(db.Text,
                      nullable=True)
    available = db.Column(db.Boolean,
                          nullable=False,
                          default=True)
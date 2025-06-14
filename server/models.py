from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

# imports, config

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# When a model class inherits from the SerializerMixin, it gains a range of methods for serializing and deserializing data.
# These methods includeto_dict()`, which converts the model object into a dictionary.
# SerializerMixin - is a superclass


class Pet(db.Model, SerializerMixin):
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)

    def __repr__(self):
        return f"<Pet {self.id}, {self.name}, {self.species}>"

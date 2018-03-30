from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import column_property

db = SQLAlchemy()


class Hero(db.Model):

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    secret_name = Column(String)
    caption = column_property(name + " (" + secret_name + ")")


    def has_alter_ego(self):
        return bool(self.secret_name)
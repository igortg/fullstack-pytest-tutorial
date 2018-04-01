from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer

db = SQLAlchemy()


class Hero(db.Model):

    id = Column(Integer, primary_key=True)
    name = Column(String)

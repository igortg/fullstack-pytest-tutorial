from flask import Flask
from flask_restalchemy import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer

app = Flask('tour-of-heroes')
db = SQLAlchemy()


class Heroe(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)


# Set an SQLite in-memory database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db.init_app(app)  # Must be called before Api object creation

api = Api(app)
api.add_model(Heroe, '/heroes')


@app.route('/create_db', methods=['POST'])
def create_db():
    db.create_all()  # Remove this in production code
    return 'DB created'


if __name__ == '__main__':
    app.run()
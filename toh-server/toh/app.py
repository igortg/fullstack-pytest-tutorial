from flask import Flask
from flask_restalchemy import Api
from toh.model import db, Hero

app = Flask("th-server")

def init_app(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(flask_app)

    api = Api(flask_app)
    api.add_model(Hero, "/heroes")


@app.route("/")
def hello():
    db.create_all()
    return "Tour of Heroes (server)!"


if __name__ == '__main__':
    init_app(app)
    app.run()

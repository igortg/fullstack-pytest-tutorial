from flask import Flask
from flask_restalchemy import Api
from toh.model import db, Heroe

app = Flask("th-server")

def init_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    db.init_app(app)

    api = Api(app)
    api.add_model(Heroe, "/heroes")


@app.route("/")
def hello():
    db.create_all()
    return "Tour of Heroes (server)!"


if __name__ == '__main__':
    init_app()
    app.run()

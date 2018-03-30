import sys
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

    if '--seed-test' in sys.argv:
        with flask_app.app_context():
            seed_test_data()


@app.route("/")
def hello():
    return "Tour of Heroes (server)!"


@app.route("/seed_test_data")
def seed_test_data():
    db.create_all()
    for test_hero in ['Wolverine', 'Cyclope', 'Nightcrawler', 'Rogue']:
        hero = Hero(name=test_hero)
        db.session.add(hero)
    db.session.commit()
    return 'DB seeded'


if __name__ == '__main__':
    init_app(app)
    app.run()

from toh.model import Hero


def test_heroe(db_session):
    heroe = Hero(name='Bombasto')
    db_session.add(heroe)
    db_session.commit()
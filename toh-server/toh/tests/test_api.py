from toh.model import Hero


def test_hero_post(client, db_session):
    response = client.post('/heroes', data={'name': 'Narco'})
    assert response.status_code == 201
    assert Hero.query.filter_by(name='Narco').count() == 1


def test_hero_get(client, db_session):
    hero = Hero(name='Bombasto')
    db_session.add(hero)
    db_session.commit()

    response = client.get('/heroes/{}'.format(hero.id))
    assert response.status_code == 200
    assert response.json == {}
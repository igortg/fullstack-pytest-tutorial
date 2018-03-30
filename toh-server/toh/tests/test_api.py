import json

from toh.model import Hero


def test_hero_get(client, db_session):
    hero = Hero(name='Superman', secret_name='Clark Kent')
    db_session.add(hero)
    db_session.commit()

    response = client.get('/heroes/{}'.format(hero.id))
    assert response.status_code == 200
    response_object = json.loads(response.data)
    assert response_object['name'] == 'Superman'
    assert response_object['secret_name'] == 'Clark Kent'

def test_hero_post(client, db_session):
    response = client.post('/heroes', data={'name': 'Narco'})
    assert response.status_code == 201
    assert Hero.query.filter_by(name='Narco').count() == 1

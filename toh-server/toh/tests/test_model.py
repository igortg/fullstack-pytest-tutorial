from toh.model import Hero


def test_hero_alter_ego():
    superman = Hero(name='Superman', secret_name='Clark Kent')
    assert superman.has_alter_ego()
    bane = Hero(name='Bane')
    assert not bane.has_alter_ego()


def test_hero(db_session):
    hero = Hero(name='Batman', secret_name='Bruce Wayne')
    db_session.add(hero)
    db_session.commit()

    batman = Hero.query.filter(Hero.caption.like('%Wayne%')).first()
    assert batman.name == 'Batman'
    assert batman.caption == 'Batman (Bruce Wayne)'

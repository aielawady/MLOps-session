from main import add


def test_add():
    assert 2 == add(1, 1)
    assert 5 == add(3, 2)
    assert -10 == add(-7, -3)

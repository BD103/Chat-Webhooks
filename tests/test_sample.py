# Examples taken from docs.pytest.org


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5

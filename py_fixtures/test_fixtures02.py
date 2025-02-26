import pytest


def test_extendList(setup01):
    setup01.extend(pytest.weekdays2)
    assert setup01 == ['mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun']

# def test_extendList(setup01):
#     setup01_copy = setup01.copy()
#     setup01_copy.extend(pytest.weekdays2)
#     assert setup01_copy == ['mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun']


def test_len(setup01, setup02):
    print(setup01)
    print(pytest.weekdays2)
    print(setup02)
    assert len(pytest.weekdays1 + setup02) == len(setup01 + pytest.weekdays2)


def test_filename(setup03):
    assert setup03.readline() == "Pytest is good.\n"

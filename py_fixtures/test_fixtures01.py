import pytest


@pytest.fixture(scope="module")
def setup_list():
    print("\n in fixture...\n")
    city = ['New York', "Paris", "Tokyo", "London"]
    return city


def test_getItem(setup_list):
    print(setup_list[1:3])
    assert setup_list[:3] == ["New York", "Paris", "Tokyo"]
    assert setup_list[1::2] == ["Paris", "London"]

@pytest.mark.xfail(reason="known issue: usefixtures can't use the fixture's return value")
@pytest.mark.usefixtures('setup_list')
def test_usefixturedemo():
    assert True
    print(setup_list[1:3])

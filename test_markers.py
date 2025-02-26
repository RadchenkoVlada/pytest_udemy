import pytest


pytestmark = [pytest.mark.smoke, pytest.mark.strtest]

@pytest.mark.sanity
def test_str01():
    num = 9/4
    s1 = 'I like ' + 'pytest automation'
    assert str(num) == '2.25'
    assert s1 == 'I like pytest automation'
    assert s1 + str(num) == 'I like pytest automation2.25'


@pytest.mark.sanity
def test_str02():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[0] == 'a'
    assert letters[-1] == 'z' == letters[25]


@pytest.mark.sanity
@pytest.mark.str
def test_str_slice():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[:] == letters
    assert letters[10:] == 'klmnopqrstuvwxyz'
    assert letters[-3:] == 'xyz'
    assert letters[:21:5] == "afkpu"


def test_str_split():
    s1 = "Python,Pytest and Automation"
    assert s1.split(',') == ['Python', 'Pytest and Automation']
    assert s1.split() == ['Python,Pytest', 'and', 'Automation']


def test_strjoin():
    s1 = "Python,Pytest and Automation"
    l1 = ["Python,Pytest", "and", "Automation"]
    l2 = ["Python", "Pytest and Automation"]
    assert ' '.join(l1) == s1


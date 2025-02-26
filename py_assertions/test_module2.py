import pytest


def test_case01():
    with pytest.raises(ZeroDivisionError):
        assert (1/0)

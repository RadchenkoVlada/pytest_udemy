import pytest


@pytest.mark.parametrize('test_input', [82, 78, 45, 66])
def test_param01(test_input):
    assert test_input > 50

@pytest.mark.parametrize('input, output', [(2,4), (3, 27), (4, 256)])
def test_param02(input, output):
    assert (input**input) == output

import pytest, sys

# XFail: mark test functions as expected to fail
@pytest.mark.xfail
def test_str04():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[100]


# this test will be - "test_xfail.py::test_str05 XPASS"
# test passes despite being expected to fail
@pytest.mark.xfail
def test_str05():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[10]


# @pytest.mark.xfail(sys.platform == 'darwin', reason="works only on MacOS")
def test_str06():
    letters = 'abcd'
    num = 1234
    assert letters + num == 'abcd1234'

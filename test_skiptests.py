import sys

import pytest

from func import cent_to_fah, const

# pytestmark = pytest.mark.skipif(sys.platform == "win32", reason="Will fail on Windows")

# pytestmark= pytest.mark.skipif(sys.platform == 'darwin', reason="Will fail on Mac")


@pytest.mark.skip(reason="Skipping for no reason")
def test_skiptests():
    assert float == type(const)


# @pytest.mark.skipif(sys.version_info > (3,8), reason="doesn't work on Python 3.8")
@pytest.mark.skipif(cent_to_fah() == 32, reason="default value test so skipping")
def test_case01():
    assert 32 == cent_to_fah()


@pytest.mark.skipif(pytest.__version__ == '8.3.4', reason="pytest version is 8.3.4")
def test_case02():
    assert cent_to_fah(38) == 100.4

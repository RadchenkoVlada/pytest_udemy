import pytest
from utils.util import get_data


@pytest.mark.parametrize("a,b,c,d", get_data())
def test_data_provider(a, b, c, d):
    print(a, b, c, d)

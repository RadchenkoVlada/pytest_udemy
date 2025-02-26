import pytest


# The 'request' fixture is a special fixture providing information of the requesting test function
@pytest.fixture(params=[(3,4), [3,5]], ids=['tuple', 'list'])
def fixture_param(request):
    with open('log.txt', 'a') as f:
        f.write(str(request.param) + '\n')
    print(request.scope)
    return request.param


# @pytest.mark.parametrize('my_fixture_param', [(3,4), [3,5]])
# def test_fixture_param02(my_fixture_param):
#     assert type(my_fixture_param) in [tuple, list]


@pytest.fixture(params=['access', 'slice'])
def fixture02(request):
    return request.param


def test_fixture_param01(fixture_param):
    assert type(fixture_param) in [tuple, list]


def test_fix_param02(fixture_param, fixture02):
    if fixture02 == 'access':
        print(fixture_param[0])
        assert fixture_param[0]
    # elif fixture02 == 'slice':
    #     print(fixture_param[::-1])
    #     assert fixture_param[::-1]






import pytest, os


def pytest_configure():
    pytest.weekdays1 = ['mon', 'tue', 'wed']
    pytest.weekdays2 = ['fri', 'sat', 'sun']
    pytest.filename = "file1.txt"


filename = "file1.txt"


@pytest.fixture(scope='function')
def setup01():
    wk1 = pytest.weekdays1.copy()
    wk1.append('thur')
    yield wk1
    print("\n After yield in setup01 \n")
    wk1.clear()
    # pytest.weekdays1.pop()


@pytest.fixture(scope='function')
def setup02():
    wk2 = pytest.weekdays2.copy()
    wk2.insert(0, 'thur')
    yield wk2
    wk2.clear()
    print("\n After yield in setup02 \n")


@pytest.fixture
def setup03():
    with open(pytest.filename, 'w') as f:
        f.write("Pytest is good.\n")
    f = open('file1.txt', 'r')
    yield f
    f.close()
    if os.path.exists(pytest.filename):
        os.remove(pytest.filename)
    print("\n After yield in setup03 \n")


@pytest.fixture
def setup04(request):
    print("\n in FIXTURE setup04 \n")
    print("\n in FIXTURE scope:" + str(request.scope))
    print("\n Calling function:" + str(request.function.__name__))
    print("\n Calling module:" + str(request.module.__name__))

import pytest, os

QA_config = 'qa.prop'
prod_config = 'prod.prop'

# it's our hook function
def pytest_addoption(parser):
    parser.addoption("--cmdopt", default='QA')

# how to start from command line: pytest -v test_argstest.py --cmdopt=QA -s
@pytest.fixture(scope='session')
def CmdOpt(pytestconfig):
    print("\n in CmdOpt fixture")
    opt = pytestconfig.getoption('cmdopt')
    if opt == 'Prod':
        f = open(prod_config, 'r')
    else:
        f = open(QA_config, 'r')
    yield f


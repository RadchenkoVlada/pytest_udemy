from pytest_bdd import scenario, given, when, then
from pathlib import Path
import pytest

featureFileDir = 'myfeatures'
featureFile = 'first101.feature'
BASE_DIR = Path(__file__).parent
FEATURE_FILE= BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

def pytest_configure():
    pytest.AMT = 0


@scenario(FEATURE_FILE, 'Withdrawal of money')
def test_withdrawal():
    print("End of Scenario Withdrawal")


@given('the account balance is 100')
def current_balance():
    pytest.AMT = 100


@when('the account holder withdraws 30')
def withdrawal_account():
    pytest.AMT = pytest.AMT - 30


@then('the account balance should be 70')
def final_balance():
    assert pytest.AMT == 70

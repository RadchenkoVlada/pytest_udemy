import pytest
from utils.myconfigparser import *
from utils.ConfigFileParser import *

config = ConfigFileParser('qa.ini')

def test_get_Gmailurl():
    print(getGmailUrl())


def test_getOutlookUrl():
    print(config.getOutlookUrl())

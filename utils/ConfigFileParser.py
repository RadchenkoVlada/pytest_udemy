import configparser
from pathlib import Path


class ConfigFileParser:
    cfgFile = 'qa.ini'  # default config file
    cfgFileDirectory = 'config'  # config directory
    config = configparser.ConfigParser()

    def __init__ (self, cfg=cfgFile):
        self.cfgFile = cfg
        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.CONFIG_FILE = self.BASE_DIR.joinpath(self.cfgFileDirectory).joinpath(self.cfgFile)
        self.config.read(self.CONFIG_FILE)

    def getGmailUrl(self):
        return self.config.get('gmail', 'url')

    def getGmailUser(self):
        return self.config.get('gmail', 'user')

    def getGmailPass(self):
        return self.config.get('gmail', 'pass')

    def getOutlookUrl(self):
        return self.config.get('outlook', 'url')


if __name__ == '__main__':
    config = ConfigFileParser('qa.ini')
    print(config.getGmailUrl())
    print(config.getGmailUser())
    print(config.getGmailPass())

    config1 = ConfigFileParser()
    print(config1.getGmailUrl())

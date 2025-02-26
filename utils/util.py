import csv

from pathlib import Path

dataFile = 'data.csv'
cfgFileDirectory = 'config'

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR.joinpath(cfgFileDirectory).joinpath(dataFile)


def get_data():
    with open(DATA_FILE) as csvfile:
        reader = csv.reader(csvfile)
        # skipping the first row
        next(reader)
        data = [tuple(row) for row in reader]
    return data

print(get_data())

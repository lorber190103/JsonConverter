import csv
import json
import sys


class JsonConverter:
    def __init__(self):
        self.data = {}

    def read_csv(self, csvFilePath: str):
        with open(csvFilePath, encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)
            for rows in csvReader:
                key = rows['Titel']
                self.data[key] = rows

    def make_json(self, jsonFilePath: str):
        with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
            jsonf.write(json.dumps(self.data, indent=4))


def main():
    csvFilePath = sys.argv[1]
    jsonFilePath = sys.argv[2]

    jsonconverter = JsonConverter()
    jsonconverter.read_csv(csvFilePath)
    jsonconverter.make_json(jsonFilePath)

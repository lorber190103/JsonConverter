import csv
import json
import sys


class JsonConverter:
    def __init__(self):
        self.data = {}

    def read_csv(self, csvFilePath: str):
        with open(f"data/{csvFilePath}", encoding='utf-8') as csv_file:
            csvReader = csv.DictReader(csv_file)
            for rows in csvReader:
                key = rows['Titel']
                self.data[key] = rows

    def make_json(self, jsonFilePath: str):
        with open(f"data/{jsonFilePath}", 'w', encoding='utf-8') as json_file:
            json_file.write(json.dumps(self.data, indent=4))


def main():
    csvFilePath = sys.argv[1]
    jsonFilePath = sys.argv[2]

    json_converter = JsonConverter()
    json_converter.read_csv(csvFilePath)
    json_converter.make_json(jsonFilePath)

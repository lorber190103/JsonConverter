import csv
import json
import sys


class JsonConverter:
    def __init__(self):
        self.data = {"Buch": []}

    def read_csv(self, csvFilePath: str):
        with open(f"data/{csvFilePath}", encoding='utf-8') as csv_file:
            csvReader = csv.DictReader(csv_file)
            for rows in csvReader:
                self.data["Book"].append(rows)

    def clean_whitespace(self, dictionary):
        return {key: value.strip() if isinstance(value, str) else value for key, value in dictionary.items()}

    def make_json(self, jsonFilePath: str):
        cleaned_data = {"Book": [self.clean_whitespace(book) for book in self.data["Book"]]}
        with open(f"data/{jsonFilePath}", 'w', encoding='utf-8') as json_file:
            json_file.write(json.dumps(cleaned_data, indent=4))


def main():
    csvFilePath = sys.argv[1]
    jsonFilePath = sys.argv[2]

    json_converter = JsonConverter()
    json_converter.read_csv(csvFilePath)
    json_converter.make_json(jsonFilePath)

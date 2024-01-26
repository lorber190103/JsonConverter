import csv
import json

from src.model import Books, db


class JsonConverter:
    def __init__(self):
        self.data = {"Buch": []}

    def read_csv(self):
        with open("src/data/input.csv", encoding='utf-8') as csv_file:
            csvReader = csv.DictReader(csv_file, skipinitialspace=True)
            for rows in csvReader:
                self.data["Buch"].append(rows)

    def make_json(self):
        with open("src/data/output.json", 'w', encoding='utf-8') as json_file:
            json_file.write(json.dumps(self.data, indent=4))


class DatabaseInserter:
    def __init__(self):
        json_converter = JsonConverter()
        json_converter.read_csv()
        json_converter.make_json()

    def insert(self):
        data = json.load(open('src/data/output.json'))
        books = data.get("Buch", [])
        for book_entry in books:
            _title = book_entry.get("Titel")
            _author = book_entry.get("Autor")
            _release_year = book_entry.get("Veroeffentlichungsjahr")
            _genre = book_entry.get("Genre")
            existing_book = Books.query.filter_by(title=_title).first()
            if not existing_book:
                db.session.add(Books(
                    title=str(_title),
                    author=str(_author),
                    release_year=str(_release_year),
                    genre=str(_genre)
                ))
        db.session.commit()

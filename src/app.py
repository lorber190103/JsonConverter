from flask import Flask, render_template

from src.main import DatabaseInserter, JsonConverter
from src.model import Books, db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///book.db"

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def user_list():
    converter = JsonConverter()
    converter.read_csv()
    converter.make_json()

    inserter = DatabaseInserter()
    inserter.insert()

    books = db.session.query(Books).order_by(Books.release_year).all()
    return render_template("books.html", books=books)

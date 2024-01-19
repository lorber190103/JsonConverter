from flask import Flask, render_template

from src.main import DatabaseInserter
from src.model import Books, db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///book.db"

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def user_list():
    inserter = DatabaseInserter()
    inserter.insert()

    books = db.session.query(Books).order_by(Books.release_year).all()
    return render_template("books.html", books=books)

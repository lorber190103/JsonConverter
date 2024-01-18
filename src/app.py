from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///book.db"

db.init_app(app)


class Books(db.Model):
    ID: Mapped[int] = mapped_column(primary_key=True)
    Author: Mapped[str]
    Release_Year: Mapped[str]
    Genre: Mapped[str]


with app.app_context():
    db.create_all()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/books")
def user_list():
    book = db.session.execute(db.select(Books).order_by(Books.Release_Year)).scalars()
    return render_template("books.html", books=book)

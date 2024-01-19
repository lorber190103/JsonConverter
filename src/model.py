from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Books(db.Model):
    ID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    author: Mapped[str]
    release_year: Mapped[str]
    genre: Mapped[str]

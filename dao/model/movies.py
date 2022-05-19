from marshmallow import Schema, fields
from setup_db import db
from sqlalchemy import Column, String, Integer, ForeignKey


class Movie(db.Model):
    """
    СОЗДАНИЕ ТАБЛИЦЫ MOVIE
    """
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(String(250))
    trailer = Column(String(250))
    year = Column(Integer)
    rating = Column(Integer)
    genre_id = Column(Integer, ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = Column(Integer, ForeignKey("director.id"))
    director = db.relationship("Director")


class MovieSchema(Schema):
    """
    ДЛЯ СЕРИАЛИЗАЦИИ
    """
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()

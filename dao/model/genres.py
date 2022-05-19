from marshmallow import Schema, fields

from setup_db import db
from sqlalchemy import Column, String, Integer


class Genre(db.Model):
    """
    СОЗДАНИЕ ТАБЛИЦЫ GENRE
    """
    __tablename__ = 'genre'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))


class GenreSchema(Schema):
    """
    ДЛЯ СЕРИАЛИЗАЦИИ
    """
    id = fields.Int(dump_only=True)
    name = fields.Str()

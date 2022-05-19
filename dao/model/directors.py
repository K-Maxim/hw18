from marshmallow import Schema, fields

from setup_db import db
from sqlalchemy import Column, String, Integer


class Director(db.Model):
    """
    СОЗДАНИЕ ТАБЛИЦЫ DIRECTOR
    """
    __tablename__ = 'director'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))


class DirectorSchema(Schema):
    """
    ДЛЯ СЕРИАЛИЗАЦИИ
    """
    id = fields.Int(dump_only=True)
    name = fields.Str()

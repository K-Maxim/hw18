from flask import Flask
from flask_restx import Api
from config import Config
from setup_db import db
from views.director import director_ns
from views.genre import genre_ns
from views.movies import movie_ns


def create_app(config):  # конфигурация БД
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    configure_app(application)
    return application


def configure_app(app):  # конфигурируем приложение
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)


if __name__ == '__main__':
    app_config = Config()  # загружаем конфигурацию
    app = create_app(app_config)  # создаем приложение
    app.run(debug=True)  # запускаем приложение


from flask import request
from flask_restx import Resource, Namespace
from container import movie_service
from dao.model.movies import MovieSchema


movie_ns = Namespace('movies')
movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        return movies_schema.dump(movie_service.get_all()), 200

    def post(self):
        post_request = request.json

        return movie_schema.dump(movie_service.create(post_request)), 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        return movie_schema.dump(movie_service.get_one(mid)), 200

    def put(self, mid):
        put_request = request.json
        put_request['id'] = mid

        return movie_schema.dump(movie_service.update(put_request)), 204

    def patch(self, mid):
        patch_request = request.json
        patch_request['id'] = mid

        return movie_schema.dump(movie_service.update_partial(patch_request)), 204

    def delete(self, mid):
        movie_service.delete(mid)

        return '', 204

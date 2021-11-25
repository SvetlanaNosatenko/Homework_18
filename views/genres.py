from flask_restx import Resource, Namespace
from implemented import genre_service
from dao.model.genre import GenreSchema, Genre
from setup_db import db

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = genre_service.get_genres()
        genre_schema = GenreSchema(many=True)
        return genre_schema.dump(all_genres), 200


@genre_ns.route('/<int:did>')
class GenreView(Resource):
    def get(self, did):
        one_genre = genre_service.one_genre(did)
        genre_schema = GenreSchema()
        return genre_schema.dump(one_genre), 200

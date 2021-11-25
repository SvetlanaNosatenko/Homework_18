# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки).
# сюда импортируются сервисы из пакета service
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service
from flask import request

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
        def get(self):
            director_id = request.args.get('director_id')
            genre_id = request.args.get('genre_id')
            year_id = request.args.get('year_id')
            movie_dict = {"director_id": director_id,
                          "genre_id": genre_id,
                          "year_id": year_id}
            all_movies = movie_service.get_movies(movie_dict)
            movie_schema = MovieSchema(many=True)
            return movie_schema.dump(all_movies), 200

        def post(self):
            data = request.json
            new_movie = movie_service.create(data)
            return "", 201, {"location": f"movies/{new_movie.id}"}


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
        def get(self, mid):
            one_movie = movie_service.one_movie(mid)
            movie_schema = MovieSchema()
            return movie_schema.dump(one_movie), 200

        def delete(self, mid):
            return movie_service.delete(mid), 204

        def put(self, mid):
            data = request.json
            if "id" not in data:
                data['id'] = mid
            movie_service.update(data)
            return "", 204

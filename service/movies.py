from dao.model.movie import Movie


class MovieService:

    def __init__(self, movie_dao):
        self.movie_dao = movie_dao

    def get_movies(self, movie_dict):
        if movie_dict.get("director_id") is not None:
            # фильмы с определенным режиссером по запросу
            result = self.movie_dao.get_by_director_id(movie_dict.get("director_id"))
        elif movie_dict.get("genre_id") is not None:
            # фильмы определенного жанра по запросу
            result = self.movie_dao.get_by_genre_id(movie_dict.get("genre_id"))
        elif movie_dict.get("year_id") is not None:
            result = self.movie_dao.get_by_year_id(movie_dict.get("year_id"))
        else:
            result = self.movie_dao.get_all_movie()
        return result

    def one_movie(self, mid):
        return self.movie_dao.get_one_movie(mid)

    def create(self, movie_id):
        return self.movie_dao.create(movie_id=movie_id)

    def delete(self, mid):
        return self.movie_dao.delete(mid=mid)

    def update(self, movie_id):
        movie = Movie(**movie_id)
        return self.movie_dao.update(movie=movie)



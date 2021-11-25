from dao.directors import DirectorDAO
from dao.genres import GenreDAO
from dao.movies import MovieDAO
from service.directors import DirectorService
from service.genres import GenreService
from service.movies import MovieService
from setup_db import db

director_dao = DirectorDAO(session=db.session)
director_service = DirectorService(director_dao=director_dao)

movie_dao = MovieDAO(session=db.session)
movie_service = MovieService(movie_dao=movie_dao)

genre_dao = GenreDAO(session=db.session)
genre_service = GenreService(genre_dao=genre_dao)


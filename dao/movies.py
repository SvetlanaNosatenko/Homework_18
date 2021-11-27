from dao.model.movie import Movie


class MovieDAO:

    def __init__(self, session):
        self.session = session

    def get_all_movie(self):
        return self.session.query(Movie).all()

    def get_by_director_id(self, val):
        return self.session.query(Movie).filter(Movie.director_id == val).all()

    def get_by_genre_id(self, val):
        return self.session.query(Movie).filter(Movie.genre_id == val).all()

    def get_by_year_id(self, val):
        return self.session.query(Movie).filter(Movie.year_id == val).all()

    def get_one_movie(self, mid):
        one_movie = self.session.query(Movie).get(mid)
        return one_movie

    def create(self, movie_id):
        new_movie = Movie(**movie_id)
        self.session.add(new_movie)
        self.session.commit()
        return ""

    def delete(self, mid):
        movie = self.get_one_movie(mid=mid)
        self.session.delete(movie)
        self.session.commit()
        return ""

    def update(self, movie_id):
        movie = self.get_one_movie(movie_id.get('id'))
        movie.title = movie_id.get('title')
        movie.description = movie_id.get('description')
        movie.trailer = movie_id.get('trailer')
        movie.year = movie_id.get('year')
        movie.rating = movie_id.get('rating')
        movie.genre_id = movie_id.get('genre_id')
        movie.director_id = movie_id.get('director_id')
        self.session.add(movie)
        self.session.commit()
        return ""
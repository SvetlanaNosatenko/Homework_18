from dao.model.genre import Genre


class GenreDAO:

    def __init__(self, session):
        self.session = session

    def get_all_genres(self):
        all_directors = self.session.query(Genre).all()
        return all_directors, 200

    def get_one_genre(self, mid):
        one_genre = self.session.query(Genre).get(mid)
        return one_genre, 200

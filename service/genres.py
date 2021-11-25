class GenreService:

    def __init__(self, genre_dao):
        self.genre_dao = genre_dao

    def get_genres(self):
        return self.genre_dao.get_all_genres()

    def one_genre(self, gid):
        return self.genre_dao.get_one_genre(gid)


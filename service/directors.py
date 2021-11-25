class DirectorService:

    def __init__(self, director_dao):
        self.director_dao = director_dao

    def get_directors(self):
        return self.director_dao.get_all_directors()

    def one_director(self, did):
        return self.director_dao.get_one_director(did)

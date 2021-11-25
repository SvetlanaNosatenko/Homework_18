from dao.model.director import Director


class DirectorDAO:

    def __init__(self, session):
        self.session = session

    def get_all_directors(self):
        all_directors = self.session.query(Director).all()
        return all_directors, 200

    def get_one_director(self, did):
        one_director = self.session.query(Director).get(did)
        return one_director, 200











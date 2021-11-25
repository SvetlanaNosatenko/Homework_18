from flask_restx import Resource, Namespace
from dao.model.director import DirectorSchema
from implemented import director_service


director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = director_service.get_directors()
        director_schema = DirectorSchema(many=True)
        return director_schema.dump(all_directors), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        one_director = director_service.one_director(did)
        director_schema = DirectorSchema()
        return director_schema.dump(one_director), 200


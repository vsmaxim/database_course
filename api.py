import psycopg2
from flask import Flask, request
from flask_restful import Resource, Api

from data import Club

app = Flask(__name__)
api = Api(app)
conn = psycopg2.connect(dbname='dogz', user='dogz', password='dogz', host='localhost', port='5432')


class ClubResource(Resource):
    def get(self, club_id):
        return Club.get_mapper(conn).get_by_id(club_id).json


class ClubListResource(Resource):
    def get(self):
        return list(map(lambda instance: instance.json, Club.get_mapper(conn).get_all()))

    def put(self):
        club = Club(None, **request.form)
        Club.get_mapper(conn).save(club)
        return '', 201


api.add_resource(ClubListResource, '/clubs')
api.add_resource(ClubResource, '/clubs/<int:club_id>')

if __name__ == '__main__':
    app.run(debug=True)
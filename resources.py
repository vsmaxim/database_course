import psycopg2
from flask_restful import Resource
from flask import request

conn = psycopg2.connect(dbname='dogz', user='dogz', password='dogz', host='localhost', port='5432')
#  Todo: request string args are array, deal with it


class ModelResource(Resource):
    data = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mapper = self.data.get_mapper(conn)


class ListCreateResource(ModelResource):
    def get(self):
        return list(map(lambda instance: instance.json, self.mapper.get_all()))

    def post(self):
        print(request.json)
        obj = self.data(None, **request.json)
        self.mapper.save(obj)
        return obj.json, 201


class RetrieveUpdateResource(ModelResource):
    def get(self, id):
        return self.mapper.get_by_id(id).json

    def put(self, id):
        obj = self.data(id, **request.json)
        self.mapper.replace(obj)
        return obj.json, 200

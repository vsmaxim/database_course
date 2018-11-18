import psycopg2
from flask_restful import Resource
from flask import request
from common.utils import permission_required

conn = psycopg2.connect(dbname='dogz', user='dogz', password='dogz', host='localhost', port='5432')
#  Todo: request string args are array, deal with it


class ModelResource(Resource):
    data = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mapper = self.data.get_mapper(conn)


class ListCreateResource(ModelResource):
    @permission_required(['administrator', 'user', ])
    def get(self):
        return list(map(lambda instance: instance.json, self.mapper.get_all()))

    @permission_required(['administrator', ])
    def post(self):
        obj = self.data(**request.json)
        self.mapper.save(obj)
        return obj.json, 201


class RetrieveUpdateResource(ModelResource):
    @permission_required(['administrator', 'user'])
    def get(self, id):
        return self.mapper.get_by_id(id).json

    @permission_required(['administrator', ])
    def put(self, id):
        obj = self.mapper.get_by_id(id)
        self.mapper.replace(obj, request.json)
        return obj.json, 200

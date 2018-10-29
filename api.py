import psycopg2
from flask import Flask, request, Response
from flask_restful import Api, Resource
from flask_cors import CORS

import resources
import data as models

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
conn = psycopg2.connect(dbname='dogz', user='dogz', password='dogz', host='localhost', port='5432')


class ClubResource(resources.RetrieveUpdateResource):
    data = models.Club


class ClubListResource(resources.ListCreateResource):
    data = models.Club


class ParticipantListResource(resources.ListCreateResource):
    data = models.Participant


class ParticipantRetrieveResource(resources.RetrieveUpdateResource):
    data = models.Participant


class BreedListResource(resources.ListCreateResource):
    data = models.Breed


class BreedRetrieveResource(resources.RetrieveUpdateResource):
    data = models.Breed


class RingListResource(resources.ListCreateResource):
    data = models.Ring


class RingRetrieveResource(resources.RetrieveUpdateResource):
    data = models.Ring


class DogListResource(resources.ListCreateResource):
    data = models.Dog


class DogRetrieveResource(resources.RetrieveUpdateResource):
    data = models.Dog


class ExpertsListResource(resources.ListCreateResource):
    data = models.Experts


class ExpertsUpdateResource(resources.RetrieveUpdateResource):
    data = models.Experts


class PrizeListResource(resources.ListCreateResource):
    data = models.Prizes


class PrizeRetrieveResource(resources.RetrieveUpdateResource):
    data = models.Prizes


class AddResultsResource(resources.ModelResource):
    data = models.Prizes

    def post(self):
        """
        data: [{
            ring_id: int,
            dog_id: int,
            place: int,
        }]
        :return:
        """
        data = request.json
        prize_objects = [self.data(**prize) for prize in data]
        for prize in prize_objects:
            self.mapper.save(prize)
        return {"message": "Prizes successfully added"}, 201


class ClubBreedsResource(resources.ModelResource):
    data = models.Club

    def get(self, id):
        return self.mapper.get_breeds(id)


class ClubPrizesResource(resources.ModelResource):
    data = models.Club

    def get(self, id):
        return self.mapper.get_prizes(id)


class BreedExpertsResource(resources.ModelResource):
    data = models.Breed

    def get(self, id):
        return self.mapper.get_experts(id)

class ExpertsBreedResource(resources.ModelResource):
    data = models.Experts

    def get(self, id):
        return self.mapper.get_dog_id(id)

api.add_resource(ClubListResource, '/clubs')
api.add_resource(ClubResource, '/clubs/<int:id>')
api.add_resource(ClubBreedsResource, '/clubs/<int:id>/breeds')
api.add_resource(ClubPrizesResource, '/clubs/<int:id>/prizes')
api.add_resource(ParticipantListResource, '/participants'),
api.add_resource(ParticipantRetrieveResource, '/participants/<int:id>')
api.add_resource(BreedListResource, '/breeds')
api.add_resource(BreedRetrieveResource, '/breeds/<int:id>')
api.add_resource(BreedExpertsResource, '/breeds/<int:id>/experts')
api.add_resource(RingListResource, '/rings')
api.add_resource(RingRetrieveResource, '/rings/<int:id>')
api.add_resource(DogListResource, '/dogs')
api.add_resource(DogRetrieveResource, '/dogs/<int:id>')
api.add_resource(ExpertsListResource, '/experts')
api.add_resource(ExpertsUpdateResource, '/experts/<int:id>')
api.add_resource(ExpertsBreedResource, '/experts/<int:id>/dog')
api.add_resource(PrizeListResource, '/prizes')
api.add_resource(PrizeRetrieveResource, '/prizes/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
from api.breed.models import Breed
from common import resources


class BreedListResource(resources.ListCreateResource):
    data = Breed


class BreedRetrieveResource(resources.RetrieveUpdateResource):
    data = Breed


class BreedExpertsResource(resources.ModelResource):
    data = Breed

    def get(self, id):
        return self.mapper.get_experts(id)
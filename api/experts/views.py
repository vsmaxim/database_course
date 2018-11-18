from flask import request

import api.experts.models
from common import resources


class ExpertsListResource(resources.ListCreateResource):
    data = api.experts.models.Experts


class ExpertsUpdateResource(resources.RetrieveUpdateResource):
    data = api.experts.models.Experts


class ExpertsBreedResource(resources.ModelResource):
    data = api.experts.models.Experts

    def get(self, id):
        return self.mapper.get_dog_id(id)

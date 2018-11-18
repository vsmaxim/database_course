import api.dog.models
from common import resources


class DogListResource(resources.ListCreateResource):
    data = api.dog.models.Dog


class DogRetrieveResource(resources.RetrieveUpdateResource):
    data = api.dog.models.Dog
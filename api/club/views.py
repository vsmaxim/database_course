import api.club.models
from common import resources


class ClubResource(resources.RetrieveUpdateResource):
    data = api.club.models.Club


class ClubListResource(resources.ListCreateResource):
    data = api.club.models.Club


class ClubBreedsResource(resources.ModelResource):
    data = api.club.models.Club

    def get(self, id):
        return self.mapper.get_breeds(id)


class ClubPrizesResource(resources.ModelResource):
    data = api.club.models.Club

    def get(self, id):
        return self.mapper.get_prizes(id)
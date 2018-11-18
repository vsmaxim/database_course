from flask import request

import api.prizes.models
from common import resources
# from common.utils import permission_required


class PrizeListResource(resources.ListCreateResource):
    data = api.prizes.models.Prizes


class PrizeRetrieveResource(resources.RetrieveUpdateResource):
    data = api.prizes.models.Prizes


class AddResultsResource(resources.ModelResource):
    data = api.prizes.models.Prizes
    # @permission_required("ppffddd")
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
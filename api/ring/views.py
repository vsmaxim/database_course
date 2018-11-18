import api.ring.models
from common import resources


class RingListResource(resources.ListCreateResource):
    data = api.ring.models.Ring


class RingRetrieveResource(resources.RetrieveUpdateResource):
    data = api.ring.models.Ring


class EmptyRingsResource(resources.ModelResource):
    data = api.ring.models.Ring

    def get(self):
        return self.mapper.get_unused_rings(), 200
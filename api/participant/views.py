import api.participant.models
from common import resources


class ParticipantRetrieveResource(resources.RetrieveUpdateResource):
    data = api.participant.models.Participant


class ParticipantListResource(resources.ListCreateResource):
    data = api.participant.models.Participant


class ParticipantRingResource(resources.ModelResource):
    data = api.participant.models.Participant

    def get(self, id):
        return self.mapper.get_ring(id)


class ParticipantReportResource(resources.ModelResource):
    data = api.participant.models.Participant

    def get(self, id):
        return self.mapper.get_report(id)
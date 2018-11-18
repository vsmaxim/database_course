from api.breed import views as breed_views
from api.club import views as club_views
from api.dog import views as dog_views
from api.experts import views as expert_views
from api.participant import views as participant_views
from api.prizes import views as prizes_views
from api.ring import views as ring_views
from api.authorization import views as authorization_views


routes = [
    (authorization_views.LoginView, '/login'),
    (club_views.ClubListResource, '/clubs'),
    (club_views.ClubResource, '/clubs/<int:id>'),
    (club_views.ClubBreedsResource, '/clubs/<int:id>/breeds'),
    (club_views.ClubPrizesResource, '/clubs/<int:id>/prizes'),
    (participant_views.ParticipantListResource, '/participants'),
    (participant_views.ParticipantRetrieveResource, '/participants/<int:id>'),
    (participant_views.ParticipantReportResource, '/participants/<int:id>/report'),
    (participant_views.ParticipantRingResource, '/participants/<int:id>/ring'),
    (breed_views.BreedListResource, '/breeds'),
    (breed_views.BreedRetrieveResource, '/breeds/<int:id>'),
    (breed_views.BreedExpertsResource, '/breeds/<int:id>/experts'),
    (ring_views.RingListResource, '/rings'),
    (ring_views.RingRetrieveResource, '/rings/<int:id>'),
    (ring_views.EmptyRingsResource, '/rings/unused'),
    (dog_views.DogListResource, '/dogs'),
    (dog_views.DogRetrieveResource, '/dogs/<int:id>'),
    (expert_views.ExpertsListResource, '/experts'),
    (expert_views.ExpertsUpdateResource, '/experts/<int:id>'),
    (expert_views.ExpertsBreedResource, '/experts/<int:id>/dog'),
    (prizes_views.PrizeListResource, '/prizes'),
    (prizes_views.PrizeRetrieveResource, '/prizes/<int:id>'),
]
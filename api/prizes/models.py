from common.mappers import Data


class Prizes(Data):
    def __init__(self, id=None, dog_id=None, place=None, ring_id=None):
        self.id = id
        self.dog_id = dog_id
        self.place = place
        self.ring_id = ring_id
        super().__init__()
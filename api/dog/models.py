from common.mappers import Data


class Dog(Data):
    def __init__(self, id=None, fancy_name=None, age=None, fathers_breed_id=None, mothers_breed_id=None, breed_id=None):
        self.id = id
        self.fancy_name = fancy_name
        self.age = age
        self.fathers_breed_id = fathers_breed_id
        self.mothers_breed_id = mothers_breed_id
        self.breed_id = breed_id
        super().__init__()

    def __str__(self):
        return self.fancy_name
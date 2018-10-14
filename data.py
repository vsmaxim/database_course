from mappers import Data


class Club(Data):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        super().__init__()

    def __str__(self):
        return self.name


class Participant(Data):
    def __init__(self, id, club_id, first_name, middle_name, last_name):
        self.id = id
        self.club_id = club_id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        super().__init__()

    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.middle_name, self.last_name)


class Breed(Data):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        super().__init__()

    def __str__(self):
        return self.name


class Ring(Data):
    def __init__(self, id, breed_id):
        self.id = id
        self.breed_id = breed_id
        super().__init__()


class Dog(Data):
    def __init__(self, id, fancy_name, age, fathers_breed, mothers_breed):
        self.id = id
        self.fancy_name = fancy_name
        self.age = age
        self.fathers_breed = fathers_breed
        self.mothers_breed = mothers_breed
        super().__init__()

    def __str__(self):
        return self.fancy_name


class Experts(Data):
    def __init__(self, participant_id, ring_id):
        self.participant_id = participant_id
        self.ring_id = ring_id
        super().__init__()


class Prizes(Data):
    def __init__(self, id, dog_id, place, ring_id):
        self.id = id
        self.dog_id = dog_id
        self.place = place
        self.ring_id = ring_id
        super().__init__()

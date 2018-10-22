from flask import request

from psycopg2.extensions import AsIs
from mappers import Data, Mapper


def get_table_name(data):
    return str(data.__class__).lower()


def get_sql_table_name(data):
    return AsIs(get_table_name(data))


class ParticipantMapper(Mapper):

    def get_ring(self, id):
        self.cursor.execute(
            """
                SELECT %(ring_table)s.id
                FROM %(participant_table)s, %(dog_table)s, %(ring_table)s,
                WHERE %(participant_table).dog_id = %(dog_table)s.id AND %(dog_table)s.breed_id == %(ring_table)s.breed_id AND %(participant_table)s.id == %(participant)s
            """,
            {
                "ring_table": get_sql_table_name(Ring),
                "participant_table": get_sql_table_name(Participant),
                "dog_table": get_sql_table_name(Dog),
                "participant": id
            }
        )
        return self.cursor.fetchall()


class ClubMapper(Mapper):

    def get_breeds(self, id):
        self.cursor.execute(
            """
                SELECT %(breed_table)s.name
                FROM %(participant_table)s, %(club_table)s, %(breed_table), %(dog_table)
                WHERE %(participant_table)s.club_id == %(club_table)s.id
                    AND %(participant_table)s.dog_id == %(dog_table)s.id 
                    AND %(dog_table)s.breed_id == %(breed_table)s.id
            """,
            {
                "participant_table": get_sql_table_name(Participant),
                "club_table": get_sql_table_name(Club),
                "breed_table": get_sql_table_name(Breed),
                "dog_table": get_sql_table_name(Dog),
            }
        )
        return self.cursor.fetchone()


class Club(Data):
    custom_mapper = ClubMapper

    def __init__(self, id, name):
        self.id = id
        self.name = name
        super().__init__()

    def __str__(self):
        return self.name


class Participant(Data):
    custom_mapper = ParticipantMapper

    def __init__(self, id, club_id, first_name, middle_name, last_name, dog_id):
        self.id = id
        self.club_id = club_id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.dog_id = dog_id
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
    def __init__(self, id, fancy_name, age, fathers_breed_id, mothers_breed_id, breed_id):
        self.id = id
        self.fancy_name = fancy_name
        self.age = age
        self.fathers_breed_id = fathers_breed_id
        self.mothers_breed_id = mothers_breed_id
        self.breed_id = breed_id
        super().__init__()

    def __str__(self):
        return self.fancy_name

# Todo: fix id
class Experts(Data):
    def __init__(self, id, participant_id = None, ring_id = None):
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

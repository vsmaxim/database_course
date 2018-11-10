from mappers import Data, Mapper
from utils import get_sql_table_name
from itertools import repeat


class ParticipantMapper(Mapper):

    def get_ring(self, id):
        self.cursor.execute(
            """
                SELECT %(ring_table)s.id
                FROM %(participant_table)s, %(dog_table)s, %(ring_table)s
                WHERE %(participant_table)s.dog_id = %(dog_table)s.id 
                    AND %(dog_table)s.breed_id = %(ring_table)s.breed_id 
                    AND %(participant_table)s.id = %(participant)s
            """,
            {
                "ring_table": get_sql_table_name(Ring),
                "participant_table": get_sql_table_name(Participant),
                "dog_table": get_sql_table_name(Dog),
                "participant": id
            }
        )
        rows = self.cursor.fetchall()
        return {"ring_id": rows[0][0] if rows else None}


class ClubMapper(Mapper):
    _places = ["first", "second", "third"]

    def get_breeds(self, id):
        self.cursor.execute(
            """
                SELECT %(breed_table)s.name
                FROM %(participant_table)s,  %(dog_table)s, %(breed_table)s
                WHERE %(participant_table)s.dog_id = %(dog_table)s.id
                    AND %(dog_table)s.breed_id = %(breed_table)s.id
                    AND %(participant_table)s.club_id = %(id)s
            """,
            {
                "participant_table": get_sql_table_name(Participant),
                "breed_table": get_sql_table_name(Breed),
                "dog_table": get_sql_table_name(Dog),
                "id": id
            }
        )
        rows = self.cursor.fetchall()
        return [row[0] for row in rows]

    def get_prizes(self, id):
        self.cursor.execute(
            """
                SELECT count(%(prize_table)s) FILTER (WHERE %(prize_table)s.place = 1) as first_place,
                       count(%(prize_table)s) FILTER (WHERE %(prize_table)s.place = 2) as second_place,
                       count(%(prize_table)s) FILTER (WHERE %(prize_table)s.place = 3) as third_place
                FROM %(prize_table)s, %(participant_table)s, %(dog_table)s, %(club_table)s
                WHERE %(prize_table)s.dog_id = %(dog_table)s.id
                    AND %(participant_table)s.dog_id = %(dog_table)s.id
                    AND %(participant_table)s.club_id = %(club_table)s.id
                    AND %(club_table)s.id = %(id)s
                GROUP BY %(club_table)s.name;
            """,
            {
                "prize_table": get_sql_table_name(Prizes),
                "participant_table": get_sql_table_name(Participant),
                "dog_table": get_sql_table_name(Dog),
                "club_table": get_sql_table_name(Club),
                "id": id
            }
        )
        rows = self.cursor.fetchall()
        prizes = rows[0] if rows else repeat(0, 3)
        return {k: v for k, v in zip(self._places, prizes)}


class BreedMapper(Mapper):

    def get_experts(self, id):
        self.cursor.execute(
            """
                SELECT %(participant_table)s.id
                FROM %(ring_table)s, %(experts_table)s, %(participant_table)s
                WHERE %(id)s = %(ring_table)s.breed_id
                    AND %(experts_table)s.ring_id = %(ring_table)s.id
                    AND %(participant_table)s.id = %(experts_table)s.participant_id
            """,
            {
                "participant_table": get_sql_table_name(Participant),
                "ring_table": get_sql_table_name(Ring),
                "experts_table": get_sql_table_name(Experts),
                "id": id,
            }
        )
        rows = self.cursor.fetchall()
        return {"expert_id": rows[0][0] if rows else None}


class ExpertsMapper(Mapper):

    def get_dog_id(self, id):
        self.cursor.execute(
            """
                SELECT %(participant_table)s.dog_id
                FROM %(experts_table)s, %(participant_table)s
                WHERE %(id)s = %(experts_table)s.ring_id
                    AND %(experts_table)s.participant_id = %(participant_table)s.id
            """,
            {
                "id": id,
                "participant_table": get_sql_table_name(Participant),
                "experts_table": get_sql_table_name(Experts)
            }
        )
        rows = self.cursor.fetchall()
        return {"dog_id": rows[0][0] if rows else None}


class Club(Data):
    custom_mapper = ClubMapper

    def __init__(self, id = None, name = None):
        self.id = id
        self.name = name
        super().__init__()

    def __str__(self):
        return self.name


class Participant(Data):
    custom_mapper = ParticipantMapper

    def __init__(self, id=None, club_id=None, first_name=None, middle_name=None, last_name=None, dog_id=None):
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
    custom_mapper = BreedMapper

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
        super().__init__()

    def __str__(self):
        return self.name


class Ring(Data):
    def __init__(self, id=None, breed_id=None):
        self.id = id
        self.breed_id = breed_id
        super().__init__()


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

class Experts(Data):
    custom_mapper = ExpertsMapper

    def __init__(self, id=None, participant_id=None, ring_id=None):
        self.id = id
        self.participant_id = participant_id
        self.ring_id = ring_id
        super().__init__()


class Prizes(Data):
    def __init__(self, id=None, dog_id=None, place=None, ring_id=None):
        self.id = id
        self.dog_id = dog_id
        self.place = place
        self.ring_id = ring_id
        super().__init__()

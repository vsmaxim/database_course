from itertools import repeat

from api.participant.models import Participant
from api.prizes.models import Prizes
from api.dog.models import Dog
from api.breed.models import Breed
from common.mappers import Mapper, Data
from common.utils import get_sql_table_name


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

    def get_report(self, id):
        self.cursor.execute(
            """
                SELECT %(participant_table)s.last_name, %(participant_table)s.first_name, 
                       %(participant_table)s.middle_name, %(prizes_table)s.place, %(dog_table)s.fancy_name,
                       %(breed_table)s.name
                FROM %(prizes_table)s, %(participant_table)s, %(dog_table)s, %(breed_table)s
                WHERE %(prizes_table)s.dog_id = %(participant_table)s.dog_id
                    AND %(participant_table)s.club_id = %(id)s
                    AND %(participant_table)s.dog_id = %(dog_table)s.id
                    AND %(dog_table)s.breed_id = %(breed_table)s.id;
            """,
            {
                "prizes_table": get_sql_table_name(Prizes),
                "participant_table": get_sql_table_name(Participant),
                "dog_table": get_sql_table_name(Dog),
                "breed_table": get_sql_table_name(Breed),
                "id": id,
            }
        )
        result_keys = ["first_name", "last_name", "middle_name", "place", "dog", "breed"]
        rows = self.cursor.fetchall()
        return [{key: value for key, value in zip(result_keys, row)} for row in rows]


class Club(Data):
    custom_mapper = ClubMapper

    def __init__(self, id = None, name = None):
        self.id = id
        self.name = name
        super().__init__()

    def __str__(self):
        return self.name
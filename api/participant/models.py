from api.prizes.models import Prizes
from api.dog.models import Dog
from api.ring.models import Ring
from common.mappers import Mapper, Data
from common.utils import get_sql_table_name


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

    def get_report(self, id):
        self.cursor.execute(
            """
                SELECT %(participant_table)s.id, %(prizes_table)s.place
                FROM %(prizes_table)s, %(participant_table)s
                WHERE %(participant_table)s.dog_id = %(prizes_table)s.dog_id
                    AND %(participant_table)s.id = %(id)s;
            """,
            {
                "participant_table": get_sql_table_name(Participant),
                "prizes_table": get_sql_table_name(Prizes),
                "id": id,
            }
        )
        result_keys = ["participant_id", "place"]
        row = self.cursor.fetchone() or [id, None]
        return {key:value for key, value in zip(result_keys, row)}


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
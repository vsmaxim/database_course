from api.participant.models import Participant
from common.mappers import Mapper, Data
from common.utils import get_sql_table_name


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


class Experts(Data):
    custom_mapper = ExpertsMapper

    def __init__(self, id=None, participant_id=None, ring_id=None):
        self.id = id
        self.participant_id = participant_id
        self.ring_id = ring_id
        super().__init__()
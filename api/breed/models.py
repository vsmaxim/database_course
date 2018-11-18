from api.participant.models import Participant
from api.ring.models import Ring
from api.experts.models import Experts
from common.mappers import Mapper, Data
from common.utils import get_sql_table_name


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


class Breed(Data):
    custom_mapper = BreedMapper

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
        super().__init__()

    def __str__(self):
        return self.name
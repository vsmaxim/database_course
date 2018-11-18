from psycopg2.extensions import AsIs

from common.mappers import Data, Mapper
from common.utils import get_sql_table_name

class RingMapper(Mapper):
    def get_unused_rings(self):
        self.cursor.execute(
            """
                SELECT %(ring_table)s.id
                FROM %(ring_table)s LEFT JOIN %(experts_table)s ON %(ring_table)s.id = %(experts_table)s.ring_id
                WHERE %(experts_table)s.id IS NULL;
            """,
            {
                "ring_table": get_sql_table_name(Ring),
                "experts_table": AsIs("experts"),
            }
        )
        return [item[0] for item in self.cursor.fetchall()]


class Ring(Data):
    custom_mapper = RingMapper

    def __init__(self, id=None, breed_id=None):
        self.id = id
        self.breed_id = breed_id
        super().__init__()
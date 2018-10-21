from data import Ring, Participant, Dog, Club, Breed
from psycopg2.extensions import AsIs

from .mappers import Mapper


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
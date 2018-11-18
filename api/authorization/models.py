from common.mappers import Data, Mapper
from common.utils import get_sql_table_name


class UsersMapper(Mapper):
    def get_password_by_username(self, username):
        self.cursor.execute(
            """
            SELECT password 
            FROM %(users_table)s 
            WHERE username = %(username)s
            """,
            {"users_table": get_sql_table_name(Users), "username": username}
        )
        row = self.cursor.fetchone() or [None]
        password = row[0]
        if not password:
            raise ValueError("There's no user")
        return password

    def get_group_by_username(self, username):
        self.cursor.execute(
            """
                SELECT %(groups_table)s.name
                FROM %(groups_table)s INNER JOIN %(users_table)s on %(groups_table)s.id = %(users_table)s.group_id
                WHERE %(users_table)s.username = %(username)s;
            """,
            {"users_table": get_sql_table_name(Users), "groups_table": get_sql_table_name(Groups), "username": username}
        )
        group = self.cursor.fetchone()[0]
        return group


class GroupsMapper(Mapper):
    pass

class Users(Data):
    custom_mapper = UsersMapper

    def __init__(self, id=None, username=None, password=None, participant_id=None, group_id=None):
        self.id = id
        self.username = username
        self.password = password
        self.participant_id = participant_id
        self.group_id = group_id


class Groups(Data):
    custom_mapper = GroupsMapper

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

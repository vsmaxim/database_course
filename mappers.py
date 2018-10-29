from abc import ABC
from typing import Type, Any, List

from psycopg2.extensions import AsIs

from utils import get_sql_table_name, SqlTranslator


class Data:
    custom_mapper = None
    # Todo: consider something about this
    id = ''

    @classmethod
    def get_mapper(cls, connection):
        if cls.custom_mapper:
            return cls.custom_mapper(connection, cls)
        else:
            return Mapper(connection, cls)

    @property
    def json(self):
        return self.__dict__

    def __str__(self):
        return '<{} object {}>'.format(self.__class__.__name__, self.id)


class FetchMixin:
    """Mixin to provide retrieving operations on database"""
    obj_class: Type[Data]
    cursor: Any
    _select_query: str = 'SELECT %(fields)s FROM %(table)s'
    _table_name: str
    _translator: SqlTranslator

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._sql_pattern = self._translator.read_pattern
        self._fields = self._translator.read_fields

    def run_select_all(self):
        """Method to perform select all expression using self.cursor"""
        self.cursor.execute(
            self._select_query,
            {
                "fields": self._sql_pattern,
                "table": self._table_name,
            }
        )

    def construct_object(self, values: tuple):
        """Method to construct object from cursor.fetch tuple"""
        return {str(key): value for key, value in zip(self._fields, values)}

    def construct_list(self):
        """Method to construct list of objects from cursor fetchall"""
        return [self.construct_object(values) for values in self.cursor.fetchall()]

    def get_all(self):
        """Method to retrieve list of objects from db"""
        self.run_select_all()
        objects = self.construct_list()
        return [self.obj_class(**data) for data in objects]

    def get_by_id(self, id):
        """Method to retrieve single object using id from db"""
        new_query = f'{self._select_query} WHERE id = %(id)s'
        self.cursor.execute(
            new_query,
            {
                "fields": self._sql_pattern,
                "table": self._table_name,
                "id": id
            }
        )
        return self.cursor.fetchone()


class WriteMixin:
    obj_class: Type[Data]
    cursor: Any
    connection: Any
    _table_name: str
    _translator: SqlTranslator

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, obj: Type[Data], commit: bool=True) -> None:
        """
        Method to save object in database

        :param obj: Instance of object
        :param commit: Commit to db
        """
        self.cursor.execute(
            """
                INSERT INTO %(table)s %(fields)s
                VALUES (%(values)s)
            """,
            {
                "table": self._table_name,
                "fields": self._translator.write_pattern,
                "values": self._translator.write_values_pattern(obj),
            }
        )
        if commit:
            self.connection.commit()

    def replace(self, diff, commit=True):
        """
        Method to update object in database

        :param diff: difference
        :param commit: Commit to database
        """
        self.cursor.execute(
            """
                UPDATE %(table)s
                SET %(replaces)s
                WHERE id = %(id)s
            """,
            {
                "table": self._table_name,
                "replaces": self._translator.update_pattern(diff),
                "id": 1 # Todo: deal with id
            }
        )
        if commit:
            self.connection.commit()


class Mapper(FetchMixin, WriteMixin):

    def __init__(self, connection, obj_class):
        self.obj_class = obj_class
        self.connection = connection
        self.cursor = connection.cursor()
        self._table_name = get_sql_table_name(self.obj_class)
        if isinstance(obj_class, type):
            obj_class = obj_class()
        self._translator = SqlTranslator(obj_class)
        super().__init__()
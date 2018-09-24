from abc import ABC

from psycopg2.extensions import AsIs


def sql_stringify(item):
    if isinstance(item, int) or isinstance(item, float):
        return str(item)
    else:
        item = str(item).replace("'", "''").replace('"', '""')
        return "'{}'".format(item)


class Data(ABC):
    custom_mapper = None
    # Todo: consider something about this
    id = ''

    @property
    def values_tuple(self):
        return AsIs('({})'.format(', '.join(map(sql_stringify, self.valuable_dict.values()))))

    @property
    def valuable_dict(self):
        ret = self.__dict__.copy()
        ret.pop('id', None)
        return ret

    @property
    def fields_tuple(self):
        return AsIs('({})'.format(', '.join(map(str, self.valuable_dict.keys()))))

    @classmethod
    def get_mapper(cls, connection):
        return cls.custom_mapper or Mapper(connection, cls)

    @property
    def json(self):
        return self.__dict__

    def __str__(self):
        return '<{} object {}>'.format(self.__class__.__name__, self.id)


class Mapper:

    def __init__(self, connection, obj_class):
        self.obj_class = obj_class
        self.table_name = self.obj_class.__name__
        self.connection = connection
        self.cursor = connection.cursor()

    @property
    def __quoteless_table_name(self):
        return AsIs(self.table_name)

    def get_by_id(self, id):
        self.cursor.execute('SELECT * FROM %s WHERE id = %s;', (self.__quoteless_table_name, id,))
        return self.obj_class(*self.cursor.fetchone())

    def get_all(self):
        self.cursor.execute('SELECT * FROM %s;', (self.__quoteless_table_name, ))
        return list(map(lambda it: self.obj_class(*it), self.cursor.fetchall()))
    
    def save(self, obj, commit=True):
        self.cursor.execute('''
        INSERT INTO %s %s
        VALUES %s;''', (self.__quoteless_table_name, obj.fields_tuple, obj.values_tuple))
        print(self.cursor.rowcount)
        if commit:
            self.connection.commit()

    def update(self, obj):
        # Todo: check how and implement update method.
        raise NotImplemented


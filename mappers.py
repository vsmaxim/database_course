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

    def __init__(self):
        for key in self.__dict__.keys():
            attr = getattr(self, key)
            if attr is not None and isinstance(attr, list):
                setattr(self, key, getattr(self, key)[0])

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

    def __validate_dict(self, dict):
        errors = {}
        for key, value in dict.items():
            if not getattr(self, key, None):
                errors[key] = 'Key is not allowed'
        return bool(errors), errors

    @staticmethod
    def __sql_update_tuple(data):
        values = map(lambda i: '{} = {}'.format(i[0], sql_stringify(*i[1])), data.items())
        return AsIs(', '.join(values))

    @property
    def replace_tuple(self):
        replace_tuple = self.__dict__.copy()
        replace_tuple.pop('id')
        return self.__sql_update_tuple(replace_tuple)

    def update_tuple(self, diff=None):
        is_valid, errors = self.__validate_dict(diff)
        if not is_valid:
            raise ValueError("Data is not valid in update dict.")
        return self.__sql_update_tuple(diff)

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


class Mapper:

    def __init__(self, connection, obj_class):
        self.obj_class = obj_class
        self.table_name = self.obj_class.__name__
        self.connection = connection
        self.cursor = connection.cursor()

    @property
    def __quoteless_table_name(self):
        return AsIs(self.table_name.lower())

    def get_by_id(self, id):
        self.cursor.execute('SELECT * FROM %s WHERE id = %s;', (self.__quoteless_table_name, id,))
        return self.obj_class(*self.cursor.fetchone())

    def get_all(self):
        self.cursor.execute('SELECT * FROM %s;', (self.__quoteless_table_name, )) # Todo: rearrange fields somehow
        return list(map(lambda it: self.obj_class(*it), self.cursor.fetchall()))
    
    def save(self, obj, commit=True):
        self.cursor.execute('''
        INSERT INTO %s %s
        VALUES %s;''', (self.__quoteless_table_name, obj.fields_tuple, obj.values_tuple))
        print(self.cursor.rowcount)
        if commit:
            self.connection.commit()

    def replace(self, obj):
        self.cursor.execute(
            'UPDATE %s SET %s WHERE id = %s;',
            (self.__quoteless_table_name, obj.replace_tuple, obj.id)
        )


from functools import wraps

from psycopg2.extensions import AsIs
from flask import session


def get_table_name(data):
    """Method to get table name (Not sql safe)"""
    return str(data.__name__).lower()


def get_sql_table_name(data):
    """Method to get sql-safe table name"""
    return AsIs(get_table_name(data))


def sql_stringify(item):
    """Function that returns sql-guarded string"""
    if item is None:
      return 'NULL'
    elif isinstance(item, int) or isinstance(item, float):
        return str(item)
    else:
        item = str(item).replace("'", "''").replace('"', '""')
        return "'{}'".format(item)


class SqlTranslator:
    """Class to retrieve sql-related fields and names"""
    def __init__(self, data):
        self._data = data
        self._data_dict = data.__dict__.copy()

    @property
    def read_fields(self):
        """Method to retrieve iterable of read fields"""
        return self._get_fields([])

    @property
    def write_fields(self):
        """Method to retrieve iterable of write fields"""
        exclude_fields = ["id", ]
        return self._get_fields(exclude_fields)

    @property
    def read_pattern(self):
        """Method to retrieve read sql pattern"""
        return AsIs(", ".join(self.read_fields))

    @property
    def write_pattern(self):
        """Method to retrieve write sql pattern"""
        fields = ", ".join(self.write_fields)
        return AsIs(f"({fields})")

    def _write_tuple(self, obj):
        """Method to generate iterable of sql strings"""
        pattern = self.write_fields
        for key in pattern:
            raw_value = getattr(obj, key)
            yield f"'{raw_value}'" if isinstance(raw_value, str) else str(raw_value)

    def write_values_pattern(self, obj): # Todo: types
        """Method to return str with values tuple that being inserted"""
        return AsIs(', '.join(self._write_tuple(obj)))

    @staticmethod
    def update_pattern(diff: dict):
        """
        Method to retrieve update sql pattern

        :param diff: difference between old and new object, represented as dict of field: value pairs
        """
        sql_safe_values = [sql_stringify(values) for values in diff.values()]
        assignment_pairs = [f"{key} = {value}" for key, value in zip(diff.keys(), sql_safe_values)]
        pattern = ", ".join(assignment_pairs)
        return AsIs(pattern)

    def _get_fields(self, exclude_keys):
        """
        Method to return tuple of dict keys

        Example: 'a, b, c, d'
        """
        copy_dict = self._data_dict.copy()
        for key in exclude_keys:
            copy_dict.pop(key, None)
        return copy_dict.keys()

# def permission_required(permission_group):
#     def decorator(view):
#         @wraps(view)
#         def wrapper(*args, **kwargs):
#             group = session.get("group", None)
#             print(session.sid)
#             if group is None:
#                 return {"message": "Unauthorized"}, 401
#             elif group != permission_group:
#                 return {"message": "You don't have permission to access this view"}, 403
#             else:
#                 return view(*args, **kwargs)
#         return wrapper
#     return decorator


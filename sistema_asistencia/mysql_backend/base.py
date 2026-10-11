from django.db.backends.mysql.base import DatabaseWrapper as MySQLWrapper
from django.db.backends.mysql.features import DatabaseFeatures as MySQLFeatures


class DatabaseFeatures(MySQLFeatures):

    can_return_columns_from_insert = False


class DatabaseWrapper(MySQLWrapper):

    features_class = DatabaseFeatures

    def check_database_version_supported(self):
        pass
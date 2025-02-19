# class MyDatabaseRouter:
#     route_app_labels = {'auth', 'contenttypes'}
    
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return 'utility'
#         return None
#     def db_for_write(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return 'utility'
#         return None
#     def allow_relation(self, obj1, obj2, **hints):
#         if(
#             obj1._meta.app_label in self.route_app_labels or
#             obj2._meta.app_label in self.route_app_labels
#         ):
#             return True
#         return None
#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label in self.route_app_label:
#             return db == 'utility'
#         return None

# class DatabaseRouter:
#     """
#     A router to control database operations on different databases.
#     """

#     def db_for_read(self, model, **hints):
#         """Direct read operations based on model"""
#         if model._meta.app_label == 'utility_app':
#             return 'utility'
#         elif model._meta.app_label == 'sql_app':
#             return 'sql_server'
#         return 'default'

#     def db_for_write(self, model, **hints):
#         """Direct write operations based on model"""
#         if model._meta.app_label == 'utility_app':
#             return 'utility'
#         elif model._meta.app_label == 'sql_app':
#             return 'sql_server'
#         return 'default'

#     def allow_relation(self, obj1, obj2, **hints):
#         """Allow relations between objects from the same database"""
#         db_set = {'default', 'utility', 'sql_server'}
#         if obj1._state.db in db_set and obj2._state.db in db_set:
#             return True
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         """Ensure migrations are run on the correct database"""
#         if app_label == 'utility_app':
#             return db == 'utility'
#         elif app_label == 'sql_app':
#             return db == 'sql_server'
#         return db == 'default'

# class UtilityDBRouter:
#     """
#     A router to control all database operations on models in the utility application.
#     """

#     def db_for_read(self, model, **hints):
#         """
#         Point all read operations for utility models to the 'utility' database.
#         """
#         if model._meta.app_label == 'utility':
#             return 'utility'
#         return None

#     def db_for_write(self, model, **hints):
#         """
#         Point all write operations for utility models to the 'utility' database.
#         """
#         if model._meta.app_label == 'utility':
#             return 'utility'
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         """
#         Ensure the utility app only appears in the 'utility' database.
#         """
#         if app_label == 'utility':
#             return db == 'utility'
#         return None


# class SQLServerDBRouter:
#     """
#     A router to control all database operations on models that need to interact with SQL Server.
#     """

#     def db_for_read(self, model, **hints):
#         """
#         Point all read operations for models that require SQL Server to the 'sql_server' database.
#         """
#         if model._meta.app_label == 'sql_server':
#             return 'sql_server'
#         return None

#     def db_for_write(self, model, **hints):
#         """
#         Point all write operations for models that require SQL Server to the 'sql_server' database.
#         """
#         if model._meta.app_label == 'sql_server':
#             return 'sql_server'
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         """
#         Ensure the SQL Server app only appears in the 'sql_server' database.
#         """
#         if app_label == 'sql_server':
#             return db == 'sql_server'
#         return None

class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'utility':
            return 'utility'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'utility':
            return 'utility'
        return 'default'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'utility':
            return db == 'utility'
        return db == 'default'
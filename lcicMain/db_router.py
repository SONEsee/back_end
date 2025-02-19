
# # class SqlServerRouter:
# #     def db_for_read(self, model, **hints):
# #         if model._meta.app_label == 'sql_server_db':
# #             return 'sql_server'
# #         return None

# #     def db_for_write(self, model, **hints):
# #         if model._meta.app_label == 'sql_server_db':
# #             return 'sql_server'
# #         return None

# #     def allow_relation(self, obj1, obj2, **hints):
# #         if obj1._meta.app_label == 'sql_server_db' or obj2._meta.app_label == 'sql_server_db':
# #             return True
# #         return None

# #     def allow_migrate(self, db, app_label, model_name=None, **hints):
# #         if app_label == 'sql_server_db':
# #             return db == 'sql_server'
# #         return None


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

# class DatabaseRouter:
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label == 'utility':
#             return 'utility'
#         elif model._meta.app_label == 'ned_sql':
#             return 'ned_sql'
#         return 'default'

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label == 'utility':
#             return 'utility'
#         elif model._meta.app_label == 'ned_sql':
#             return 'ned_sql'
#         return 'default'

#     def allow_relation(self, obj1, obj2, **hints):
#         db_set = {'default', 'utility', 'ned_sql'}
#         if obj1._state.db in db_set and obj2._state.db in db_set:
#             return True
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label == 'utility':
#             return db == 'utility'
#         elif app_label == 'ned_sql':
#             return db == 'ned_sql'
#         return db == 'default'


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
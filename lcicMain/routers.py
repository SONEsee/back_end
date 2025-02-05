
class SqlServerRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'sql_server_db':
            return 'sql_server'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'sql_server_db':
            return 'sql_server'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'sql_server_db' or obj2._meta.app_label == 'sql_server_db':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'sql_server_db':
            return db == 'sql_server'
        return None
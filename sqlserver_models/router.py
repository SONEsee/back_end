class NEDRouter:
    # def db_for_read(self, model, **hints):
    #     if getattr(model, 'is_ned_model', False):
    #         return 'sql_server'
    #     return None

    # def db_for_write(self, model, **hints):
    #     if getattr(model, 'is_ned_model', False):
    #         return 'sql_server'
    #     return None

    # def allow_migrate(self, db, app_label, model_name=None, **hints):
    #     if db == 'sql_server':
    #         return False
    #     return None
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'sqlserver_models':
            return 'sql_server'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'sqlserver_models':
            return 'sql_server'
        return None
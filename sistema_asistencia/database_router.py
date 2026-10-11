class DatabaseRouter:

    def db_for_read(self, model, **kwargs):

        if model._meta.model_name == 'registrohistorico':
            return 'mysql'

        return 'default'


    def db_for_write(self, model, **kwargs):

        if model._meta.model_name == 'registrohistorico':
            return 'mysql'

        return 'default'


    def allow_relation(self, obj1, obj2, **kwargs):

        return True


    def allow_migrate(self, db, app_label, model_name=None, **kwargs):

        if model_name == 'registrohistorico':
            return db == 'mysql'

        return db == 'default'
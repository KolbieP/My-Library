class PublicLibraryRouter:
    """
    A router to control all database operations on models in the public library application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read public library models go to public_library.
        """
        if model._meta.app_label == 'public_library':
            return 'public_library'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write public library models go to public_library.
        """
        if model._meta.app_label == 'public_library':
            return 'public_library'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the public library app is involved.
        """
        if obj1._meta.app_label == 'public_library' or obj2._meta.app_label == 'public_library':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the public library app only appears in the 'public_library' database.
        """
        if db == 'public_library':
            return model_name == 'publicbook' and app_label == 'BookListAPI'
        return None

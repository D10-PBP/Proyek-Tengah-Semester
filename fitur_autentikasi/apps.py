from django.apps import AppConfig


class FiturAutentikasiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fitur_autentikasi'

    def ready(self):
        import fitur_autentikasi.signals
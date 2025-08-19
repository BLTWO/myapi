from django.apps import AppConfig
import sys


class ResumeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "resume"

    def ready(self):
        from . import resumefetch

        if 'runserver' in sys.argv:
            resumefetch.fetch_and_update_resume()

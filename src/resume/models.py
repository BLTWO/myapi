from django.db import models

# Create your models here.
class Resume(models.Model):
    resume_uri = models.URLField(default='', blank=True)
    date = models.DateTimeField(null=True, blank=True)

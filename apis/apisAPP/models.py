from django.db import models

class Entry(models.Model):
    api = models.CharField(verbose_name="api", max_length=250)
    description = models.CharField(verbose_name="Description", max_length=500)
    auth = models.CharField(verbose_name="Auth", max_length=250)
    https =  models.BooleanField(verbose_name="https")
    cors = models.CharField(verbose_name="Cors", max_length=250)
    link = models.CharField(verbose_name="Link", max_length=250)
    category = models.CharField(verbose_name="Category", max_length=250)

    class Meta:
        app_label = 'apisAPP'
        verbose_name = 'Entry'

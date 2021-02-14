from django.db import models


class ActiveobjectsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Markets(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(null=True)

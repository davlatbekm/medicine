from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True)
    adres = models.CharField(max_length=200)
    city = models.CharField(max_length=50)

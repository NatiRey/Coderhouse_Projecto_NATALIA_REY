from ctypes import addressof
from django.db import models


class Atelier(models.Model):
    atelier = models.CharField(max_length=40)
    address = models.IntegerField()
    description = models.TextField(blank = True, null=True)


    def __str__(self):
        return f'{self.atelier} atelier --'
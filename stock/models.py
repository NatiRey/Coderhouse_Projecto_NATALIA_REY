from django.db import models


class Stock(models.Model):
    piece = models.CharField(max_length=40)
    add_date = models.DateField()
    is_available = models.BooleanField()

    def __str__(self):
        is_available = 'Si' if self.is_delivered else 'No'
        return f'Art piece: {self.piece} -- Created on: {self.add_date} -- Available: {is_available}'


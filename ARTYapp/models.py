from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    artist_name = models.CharField(max_length=20)
    art_fields = models.TextField()
    country = models.CharField(max_length=16)
    email = models.EmailField()

    def __str__(self):
        return f'Full name: {self.name} {self.last_name}, from: {self.country} -- e-mail: {self.email} -- Artistic name: {self.artist_name}, Art fields: {self.art_fields} '


class Project(models.Model):
    project_name = models.CharField(max_length=40)
    project_type = models.CharField(max_length=40)
    description = models.TextField()
    add_date = models.DateField()

    def __str__(self):
        return f'Art Proyect: {self.name} -- Type: {self.proyect_type} -- Description: {self.description} -- Created on: {self.add_date} --'


class Stock(models.Model):
    Art_piece = models.CharField(max_length=40)
    Art_type = models.CharField(max_length=40)
    description = models.TextField()
    price = models.IntegerField
    available = models.BooleanField()

    def __str__(self):
        available = 'Yes' if self.available else 'No'
        return f'Art piece: {self.Art_piece}, Type: {self.art_type} -- Available: {available} -- Price: {self.price} -- Description: {self.description}'
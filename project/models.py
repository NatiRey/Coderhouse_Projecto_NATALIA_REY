from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=40)
    description = models.TextField(blank = True, null=True)

    def __str__(self):
        return f'Project: {self.name} -- {self.type} -- {self.description}'

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=192, unique=True)
    first_name = models.CharField(max_length=192)
    last_name = models.CharField(max_length=192, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Group(models.Model):
    name = models.CharField(max_length=128)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

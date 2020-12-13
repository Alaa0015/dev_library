from django.db import models

class Developer(models.Model):
    name = models.CharField(max_length=42)
    description = models.CharField(max_length=124)
    def __str__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField(max_length=42)
    description = models.CharField(max_length=124)
    def __str__(self):
        return self.name

class Topic(models.Model):
    title = models.CharField(max_length=42)
    description = models.CharField(max_length=124)
    developer = models.ManyToManyField(Developer)
    theme = models.ManyToManyField(Theme)
    def __str__(self):
        return self.title
from django.db import models
from django.db.models.fields import CharField, DateField, TextField

# Create your models here.
class Blog(models.Model):

    title = models.CharField(max_length=20)
    date = models.DateField()
    desc = models.TextField()

    def __str__(self):
        return self.title


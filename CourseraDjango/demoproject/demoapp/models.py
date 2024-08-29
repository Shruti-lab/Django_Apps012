from django.db import models
from unicodedata import name

# Create your models here.
class Menu(models.Model):
    person_name = models.CharField(max_length=50);
    cuisine = models.CharField(max_length=50);
    price = models.IntegerField();
    age = models.IntegerField();

    def __str__(self):
        return self.name + " : " + self.cuisine



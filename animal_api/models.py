from django.db import models

# Create your models here.

ANIMAL_CHOICES = (
        ('Herbivore', 'Herbivore'),
        ('Carnivore', 'Carnivore'),
    )

class Animal(models.Model):
    name = models.CharField(max_length=100,unique=True)
    type = models.CharField(choices=ANIMAL_CHOICES, max_length=20)
    sound = models.CharField(max_length=100)
    extra_information = models.TextField(blank=True, null=True)
from django.db import models

# Create your models here.
class Meetup(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(unique=True)
    description=models.CharField(max_length=100)
    image=models.ImageField('image')

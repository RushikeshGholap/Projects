from django.db import models

# Create your models here.

class Document(models.Model):
	des = models.CharField(max_length=100)
	image = models.ImageField(upload_to='media/')

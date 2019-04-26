from django.db import models

# Create your models here.

class numbers(models.Model):
	a = models.IntegerField()
	b = models.IntegerField()
	result = models.IntegerField(default=0)
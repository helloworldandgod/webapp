from django.db import models

# Create your models here.
class Company(models.Model):
	name = models.CharField(max_length=20)
	ticker = models.CharField(max_length=10)

	def __str__(self):
		return self.name

class Market(models.Model):
	name = models.CharField(max_length=10)
	companies = models.ManyToManyField(Company)

	def __str__(self):
		return self.name

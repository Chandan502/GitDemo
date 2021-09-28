from django.db import models

class Product(models.Model):
	pno = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	price = models.IntegerField()

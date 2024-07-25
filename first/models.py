from django.db import models

# Create your models here.
class Carmodel(models.Model):
    class Meta:
        db_table = 'Cars'
    brand=models.CharField(max_length=50)
    price=models.IntegerField()
    year=models.IntegerField()
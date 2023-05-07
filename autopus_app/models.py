from django.db import models

# Create your models here.
class Product(models.Model):
    tittle=models.CharField(max_length=200)
    warnty=models.IntegerField()
    created_on=models.DateTimeField(auto_now_add=True)
    price=models.IntegerField()
    desc=models.CharField(max_length=200)
    
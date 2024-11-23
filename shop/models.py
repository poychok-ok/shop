from django.db import models

# Create your models here.
class Product(models.Model):
    price = models.PositiveIntegerField()
    name = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField()
    descrition = models.TextField()
    img = models.ImageField(upload_to='images/')
    discounts = models.PositiveIntegerField(default=0)
    ratind = models.FloatField(default=0.0)
    is_avalable = models.BooleanField(default=True)



class Orderssssss(models.Model):
    Product= models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    telephone =models.CharField(max_length=15)
    address = models.CharField(max_length=60)
    email = models.CharField(max_length=70)
    quantity = models.PositiveIntegerField(default=1)
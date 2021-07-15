from django.db import models


# Create your models here.
class Product(models.Model):
    
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products', null=True)
    categoty=models.CharField(max_length=60)
    description = models.TextField()
    price=models.IntegerField()
    available_items=models.IntegerField()

    def __str__(self):
        return self.name

   

class Order(models.Model):
    date = models.DateField(auto_now=True)
    product=models.ForeignKey(Product, on_delete=models.SET_NULL,related_name='orders',null=True)



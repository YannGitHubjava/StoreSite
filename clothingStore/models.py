from django.db import models
from django.utils.encoding import smart_text

# Create your models here.




class Product(models.Model):
    """Product table stores all item informations
       and manipulate their info"""
    productID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, default="Item")
    price = models.DecimalField(max_digits= 5, null=False, decimal_places=2, default=0)
    genre = models.CharField(max_length=10, null=True, default="male")
    catergory = models.CharField(max_length=25, null=False)
    description = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True, upload_to="clothingStore/")
    quantity = models.IntegerField(default=0, null=False)

    pmg = models.Manager()



class Customer(models.Model):
    """Customer table stores all item informations
        and manipulate their info"""

    customerId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=True)



class orderLine(models.Model):
    """ productLine table stores all sold item and
            customers to manipulate their info"""

    customerId = models.ForeignKey(Customer)
    productId = models.OneToOneField(Product)
    qty = models.IntegerField(default=0, null=False)




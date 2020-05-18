from django.db import models

# Create your models here.



class Product(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    images=models.ImageField(upload_to='images//',null=True)
    price=models.IntegerField()
    catagory=models.CharField(max_length=50,default='electronics',choices=(("electronics","electronics"),("clothing","clothing"),("vehicle","vehicle")))
    def __str__(self):
        return self.name


class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phone=models.CharField(max_length=16)
    desc=models.CharField(max_length=500)
    def __str__(self):
        return self.name
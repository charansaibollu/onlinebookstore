from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    bid = models.IntegerField(primary_key=True)
    bname = models.CharField(max_length=20)
    bcost = models.DecimalField(max_digits=10, decimal_places=2)
    bauthor = models.CharField(max_length=20)
    bpdate= models.DateField()
    def __str__(self):
        return self.bname


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.user)


class Cart(models.Model):
    customer = models.OneToOneField(Customer, null=True, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return str(self.customer)





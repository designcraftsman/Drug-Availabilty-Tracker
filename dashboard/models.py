from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)

class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

class Order(models.Model):
    medicine_name = models.CharField(max_length=100)
    expire_date = models.DateField()
    quantity = models.IntegerField()
    batch_no = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
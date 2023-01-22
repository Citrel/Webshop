from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    Address_ID = models.BigAutoField(primary_key=True)
    plz = models.CharField(max_length=10)
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)

class Warehouse(models.Model):
    Warehouse_ID = models.BigAutoField(primary_key=True)
    address_id = models.OneToOneField(Address, on_delete=models.CASCADE)

class Customer(models.Model):
    Customer_ID = models.BigAutoField(primary_key=True)
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    current_delivery_address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    current_billing_address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)

class Category(models.Model):
    Category_ID = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    category_description = models.CharField(max_length=800)

class Product(models.Model):
    Product_ID = models.BigAutoField(primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=800)
    product_image_path = models.ImageField(upload_to='products/')
    price = models.FloatField()
    date_last_change = models.DateField(auto_now=True)
    delivery_time = models.IntegerField(min)

class Product_Availability(models.Model):
    Product_ID = models.ForeignKey(Product, on_delete=models.CASCADE)
    Warehouse_ID = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    available_amount = models.IntegerField()

class Order(models.Model):
    Order_ID = models.BigAutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)

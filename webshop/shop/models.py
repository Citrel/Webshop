from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Category(models.Model):
    Category_ID = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    category_description = models.CharField(max_length=800)

class Payment_Method(models.Model):
    Payment_Method_ID = models.BigAutoField(primary_key=True)
    method_name = models.CharField(max_length=100)
    method_fee = models.FloatField()

class Address(models.Model):
    Address_ID = models.BigAutoField(primary_key=True)
    plz = models.CharField(max_length=10)
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)

class Product(models.Model):
    Product_ID = models.BigAutoField(primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=800)
    product_image_path = models.ImageField(upload_to='products/')
    price = models.FloatField()
    date_last_change = models.DateField(auto_now=True)
    delivery_time = models.PositiveIntegerField(min)

class Warehouse(models.Model):
    Warehouse_ID = models.BigAutoField(primary_key=True)
    address_id = models.OneToOneField(Address, on_delete=models.CASCADE)
    product_availability = models.ManyToManyField(Product, through='Product_Availability')

class Customer(models.Model):
    Customer_ID = models.BigAutoField(primary_key=True)
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    current_delivery_address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    current_billing_address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    cart = models.ManyToManyField(Product, through='Cart')

class Product_Availability(models.Model):
    Product_ID = models.ForeignKey(Product, on_delete=models.CASCADE)
    Warehouse_ID = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    available_amount = models.PositiveIntegerField()

class Order(models.Model):
    Order_ID = models.BigAutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_method_id = models.ForeignKey(Payment_Method, on_delete=models.CASCADE)
    payment_address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    payed = models.BooleanField()
    order_date = models.DateField(auto_now_add=True)
    products_per_order = models.ManyToManyField(Product, through='Products_per_Order')
    delivery = models.ManyToManyField(Address, through='Delivery')

class Products_per_Order(models.Model):
    Order_ID = models.ForeignKey(Order, on_delete=models.CASCADE)
    Product_ID = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_amount = models.PositiveIntegerField()
    product_price_at_order_time = models.FloatField()
    
class Delivery(models.Model):
    Order_ID = models.ForeignKey(Order, on_delete=models.CASCADE)
    Delivery_Address_ID = models.ForeignKey(Address, on_delete=models.CASCADE)
    warehouse_id = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    delivery_date = models.DateField()

class Cart(models.Model):
    Customer_ID = models.ForeignKey(Customer, on_delete=True)
    Product_ID = models.ForeignKey(Product, on_delete=True)
    cart_amount = models.PositiveIntegerField()

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from profiles.models import Profile, User_Payment_Address, User_Delivery_Address


class Category(models.Model):
    Category_ID = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    category_description = models.CharField(max_length=800)


class Payment_Method(models.Model):
    Payment_Method_ID = models.BigAutoField(primary_key=True)
    method_name = models.CharField(max_length=100)
    method_fee = models.FloatField()


class Product(models.Model):
    Product_ID = models.BigAutoField(primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=800)
    product_image_path = models.ImageField(upload_to='webshop/static/images')
    price = models.FloatField()
    date_last_change = models.DateField(auto_now=True)
    delivery_time = models.PositiveIntegerField(min)
    Selected = models.BooleanField(default=False)


class Order(models.Model):
    Order_ID = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    payment_method_id = models.ForeignKey(
        Payment_Method, on_delete=models.CASCADE)
    payment_address_id = models.ForeignKey(
        User_Payment_Address, on_delete=models.CASCADE, related_name='payment_address')
    payed = models.BooleanField()
    order_date = models.DateField(auto_now_add=True)
    products_per_order = models.ManyToManyField(
        Product, through='Products_per_Order')
    delivery = models.ForeignKey(
        User_Delivery_Address, on_delete=models.CASCADE, related_name='delivery')


class Products_per_Order(models.Model):
    Order_ID = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='in_the_order')
    Product_ID = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_amount = models.PositiveIntegerField()
    product_price_at_order_time = models.FloatField()


class Delivery(models.Model):
    Order_ID = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='deliverys_order_id')
    Delivery_Address_ID = models.ForeignKey(
        User_Delivery_Address, on_delete=models.CASCADE, related_name='delivery_address')
    delivery_date = models.DateField()


class Cart(models.Model):
    Customer_ID = models.ForeignKey(
        Profile, on_delete=models.CASCADE, default=None)
    product_key = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product', default=None)
    cart_amount = models.PositiveIntegerField()


class Product_Likes(models.Model):
    Customer_ID = models.ForeignKey(
        Profile, on_delete=models.CASCADE, default=None)
    Product_ID = models.ForeignKey(Product, on_delete=models.CASCADE)

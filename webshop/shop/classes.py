from .models import *

# Definiert Klassen die sich direkt auf die models.py beziehen
# Wird für die Controller benötigt


class Products:
    def __init__():
        product_name = Product.objects.values('product_name')
        product_category = Product.objects.select_related('category_name')
        product_image = Product.objects.values('product_image_path')
        price = Product.objects.values('price')
        product_description = Product.objects.values('product_description')
        date = Product.objects.values('date_last_change')
        delivery_time = Product.objects.values('delivery_time')

        def get_product_name():
            return product_name

        def set_product_name(input_name):
            product_name = input_name

        def get_product_category():
            return product_category

        def set_product_name(input_category):
            product_category = input_category

        def get_product_image():
            return product_image

        def set_product_image(input_image):
            product_image = input_image

        def get_price():
            return price

        def set_price(input_price):
            price = input_price

        def get_product_description():
            return product_description

        def set_product_description(input_description):
            product_description = input_description

        def get_date():
            return date

        def set_date(input_date):
            date = input_date

        def get_delivery_time():
            return delivery_time

        def set_delivery_time(input_time):
            delivery_time = input_time

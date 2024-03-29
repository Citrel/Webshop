from django.contrib import admin
from .models import Category, Product
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_description')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_description',
                    'product_image_path', 'price', 'delivery_time')
    readonly_fields = ('date_last_change',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

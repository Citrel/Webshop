from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *


class Homepage:

    def show_products(request):
        
        products = Product.objects.all()
        
        return render (request, 'index.html', {'products' : products})
    

class Categories:
    
    def show_categories(request, pk):
        
        category = Category.objects.all()
        
        productList = get_object_or_404(Product, pk = pk)
        
        return render(request, 'categories.html', {'category' : category, 'productList' : productList})
    
    
class About_Us:
    
    def show_Abouts():
        
        return render('About_Us.html')
    

class Impressum:
    
    def show_Impressum():
        
        return render('Impressum.html')
    

class AGB:
    
    def show_AGB():
        
        return render('AGB.html')
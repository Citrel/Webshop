from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.db.models import Q


class Homepage:

    def show_products(request):
        
        products = Product.objects.all()
        
        return render (request, 'index.html', {'products' : products})
    

class Categories:
    
    def show_categories(request, pk):
        
        category = Category.objects.all()
        
        productList = get_object_or_404(Product, pk = pk)
        
        return render(request, 'categories.html', {'category' : category, 'productList' : productList})
    

class Search:

        def show_searched_products(request):
            
            results = []
            
            if request.method == "GET":
                query = request.GET.get('search')
                
                if query == '':
                    query = 'None'
                    
                result = Product.objects.filter(Q(product_name__icontains=query) | Q(product_description_icontains=query))
                
                return render(request, 'search.html', {'query' : query, 'result' : result})
            
           
class Cart:
    
    def show_cart(request, pk):
        
        product = Product.objects.all()
        customer = Customer.objects.all()
        cart_objects = get_object_or_404(Cart, pk = Cart.Customer_ID)
        
        return render(request, 'cart.html', {'product' : product, 'customer' : customer, 'cart_objects' : cart_objects})
    
            
        
    
class About_Us:
    
    def show_Abouts():
        
        return render('About_Us.html')
    

class Impressum:
    
    def show_Impressum():
        
        return render('Impressum.html')
    

class AGB:
    
    def show_AGB():
        
        return render('AGB.html')


class Profile:

    def show_profile(request):

        customer = Customer.objects.all()

        return render(request, 'profile.html', {'customer' : customer})
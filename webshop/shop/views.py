from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Q, Sum
import random


class Homepage:

    def show_products(request):
        
        products = Product.objects.all()
        
        return render (request, 'index.html', {'products' : products})
    

class Article():
    
    def show_information(request, pk):
        
        product = get_object_or_404(Product, pk=pk)
        eyes = random.randint(14, 3507)
        likes = Product_Likes.objects.filter(Product_ID = pk).count() 
        
        
        return render(request, 'product_detail.html',{'product' : product, 'they_are_watching_us' : eyes, 'likes' : likes})
    
    def like_product(request, pkProduct, pkCustomer):
        
        likes = Product_Likes.objects.filter(Product_ID = pkProduct).count()       
        liked = get_object_or_404(Product_Likes, Customer_ID = pkCustomer, Product_ID = pkProduct)
        
        if request.method == 'GET':
            
            if liked == None:
                
                Product_Likes.objects.create(pkCustomer, pkProduct)
            
            return redirect('product_detail', pk=pkProduct)
        
        return render(request, 'product_detail.html', {'likes':likes})
                

class Categories:
    
    def show_categories(request, pk):
        
        category = Category.objects.all()
        
        productList = get_object_or_404(Product, pk = pk)
        
        return render(request,'categories.html', {'category' : category, 'productList' : productList})
    

class Search:

        def show_searched_products(request):
            
            results = []
            
            if request.method == "GET":
                query = request.GET.get('search')
                
                if query == '':
                    query = 'None'
                    
                result = Product.objects.filter(Q(product_name__icontains=query) | Q(product_description__icontains=query))
                
                return render(request, 'search.html', {'query' : query, 'result' : result})
            
           
class Cart:
    
    def show_cart(request, pk):
        
        product = Product.objects.all()
        customer = Customer.objects.all()
        cart_objects = get_object_or_404(Cart, pk = Cart.Customer_ID)
        
        return render(request, 'cart.html', {'product' : product, 'customer' : customer, 'cart_objects' : cart_objects})
    
    
    def payment_sum(request, pk):
        
        cart_objects = get_object_or_404(Cart, pk = Cart.Customer_ID)
        
        total_cost = cart_objects.objects.aggregate(Sum('cart_objects.Product.price') * cart_objects.cart_amount)
        
        
        
        
        return render(request, 'cart.html', {'total_cost' : total_cost})
        
    
    
        
    
class About_Us:
    
    def show_abouts(request):
        
        return render(request, 'about_us.html')
    

class Imprint:
    
    def show_imprint():
        
        return render('imprint.html')
    


class Profile:

    def show_profile(request):

        customer = Customer.objects.all()

        return render(request, 'myprofil.html', {'customer' : customer})
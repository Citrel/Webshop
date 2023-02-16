from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Q, Sum, Count
import random


class Homepage:

    def show_products(request):

        products = Product.objects.all()
        categories = Category.objects.all()
        cart_item_count = Cart.objects.filter(Customer_ID=request.user.id).count()
        
        return render (request, 'index.html', {'products' : products, 'categories' : categories, 'cart_item_count' : cart_item_count})
    

class Article():
    
    def show_information(request, pk):
        
        cart_item_count = Cart.objects.filter(Customer_ID=request.user.id).count()
        
        product = get_object_or_404(Product, pk=pk)
        likes = Product_Likes.objects.filter(Product_ID = pk).count() 
        
        
        return render(request, 'product_detail.html',{'product' : product, 'likes' : likes, 'cart_item_count' : cart_item_count})
    
    def like_product(request, pk):
              
        liked = get_object_or_404(Product_Likes, Customer_ID = request.user.id, Product_ID = pk)
        
        if request.method == 'GET':
            
            if liked == None:
                
                liked = Product_Likes(Customer_ID=request.user.id, Product_ID=pk)
                liked.save()
            
            return redirect('product_detail', pk=pk)
        
        return render(request, 'product_detail.html')
                

class Categories:

    def show_categories(request, pk):
        
        cart_item_count = Cart.objects.filter(Customer_ID=request.user.id).count()
        
        category = get_object_or_404(Category, pk=pk)
        
        product_list = Product.objects.filter(category_id__Category_ID__contains=pk)
        
        return render(request,'category.html', {'category' : category, 'product_list' : product_list, 'cart_item_count' : cart_item_count})
    

class Search:

        def show_searched_products(request):
            
            cart_item_count = Cart.objects.filter(Customer_ID=request.user.id).count()
            
            results = []
            
            if request.method == "GET":
                query = request.GET.get('search')
                
                if query == '':
                    query = 'None'
                    
                result = Product.objects.filter(Q(product_name__icontains=query) | Q(product_description__icontains=query))
                
                return render(request, 'search.html', {'query' : query, 'result' : result, 'cart_item_count' : cart_item_count})
            
           
class Cart_View:

    def show_cart(request):
        
        cart_item_count = Cart.objects.filter(Customer_ID=request.user.id).count()

        cart_objects = Cart.objects.filter(Customer_ID = request.user)
        product = Product.objects.filter(Product_ID=Cart.Product_ID)

        return render(request, 'cart.html', {'product': product, 'cart_objects': cart_objects, 'cart_item_count' : cart_item_count})
    


class About_Us:

    def show_abouts(request):
        
        cart_item_count = Cart.objects.filter(Customer_ID=request.user.id).count()

        return render(request, 'about_us.html', {'cart_item_count' : cart_item_count})


class Imprint:

    def show_imprint(request):
        
        cart_item_count = Cart.objects.filter(Customer_ID=request.user.id).count()

        return render(request, 'imprint.html', {'cart_item_count' : cart_item_count})

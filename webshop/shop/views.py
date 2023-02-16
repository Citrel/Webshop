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
        cart_item_count = Cart.objects.filter(Customer_id=request.user).Count()
        
        return render (request, 'index.html', {'products' : products, 'categories' : categories, 'cart_item_count' : cart_item_count})
    

class Article():
    
    def show_information(request, pk):
        
        product = get_object_or_404(Product, pk=pk)
        likes = Product_Likes.objects.filter(Product_ID = pk).count() 
        
        
        return render(request, 'product_detail.html',{'product' : product, 'likes' : likes})
    
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
        
        category = get_object_or_404(Category, pk=pk)
        
        product_list = Product.objects.filter(category_id__Category_ID__contains=pk)
        
        return render(request,'category.html', {'category' : category, 'product_list' : product_list})
    

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
        cart_objects = get_object_or_404(Cart, pk=Cart.Customer_ID)

        return render(request, 'cart.html', {'product': product, 'customer': customer, 'cart_objects': cart_objects})

    def payment_sum(request, pk):

        cart_objects = get_object_or_404(Cart, pk=Cart.Customer_ID)

        total_cost = cart_objects.objects.aggregate(
            Sum('cart_objects.Product.price') * cart_objects.cart_amount)

        return render(request, 'cart.html', {'total_cost': total_cost})


class About_Us:

    def show_abouts(request):

        return render(request, 'about_us.html')


class Imprint:

    def show_imprint(request):

        return render(request, 'imprint.html')

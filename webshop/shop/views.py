from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from profiles.models import Profile
from .forms import *
from django.db.models import Q, Sum, Count
from django.http import Http404
from django import template
from django.contrib.auth.models import User



class Homepage:

    def show_products(request):

        products = Product.objects.all()
        categories = Category.objects.all()
        cart_item_count = Cart.objects.filter(Customer_ID=request.user.id).count()
        
        return render (request, 'index.html', {'products' : products, 'categories' : categories, 'cart_item_count' : cart_item_count})
    

class Article():
    
    def show_information(request, pk):
        
        cart_item_count = Cart.objects.filter(Customer_ID=request.user.id).count()
        categories = Category.objects.all()
        
        product = get_object_or_404(Product, pk=pk)
        likes = Product_Likes.objects.filter(Product_ID = pk).count() 
        
        
        return render(request, 'product_detail.html',{'product' : product, 'likes' : likes, 'cart_item_count' : cart_item_count, 'categories' : categories})
    
    def like_product(request, pk):
        
        
        if request.method == 'POST':
            likedProduct = Product.objects.get(Product_ID = pk)
            is_liked = True
        
            liked, created = Product_Likes.objects.get_or_create(defaults={'Product_ID': likedProduct}, Customer_ID_id= request.user.id, Product_ID = likedProduct)
        
        
            if not created:
                liked.delete()
                is_liked = False
            else:
                liked.save()
                is_liked = True
            
        
            return redirect('details', pk = pk)
        return render(request,'product_detail.html' , {'is_liked' : is_liked})
    
    
    def add_to_cart(request, pk):
        
        if request.method == 'POST':
            amount = int(request.POST.get('change_article_amount'))
            
            product_obj = Product.objects.get(Product_ID=pk)
        
        if amount > 0:
            created = Cart.objects.filter(Customer_ID = request.user.id, product_key = product_obj).exists()
        
            if not created:
                new_entry = Cart.objects.create(Customer_ID_id = request.user.id, product_key = product_obj, cart_amount = amount)
                new_entry.save()
            else:
                existing_entry = Cart.objects.get(Customer_ID_id = request.user.id, product_key = product_obj)
                existing_entry.cart_amount += amount
                existing_entry.save()
            
            return redirect('cart')
        
        return render(request, 'cart.html')
    
    
    

class Categories:

    def show_categories(request, pk):
        
        cart_item_count = Cart.objects.filter(Customer_ID=request.user.id).count()
        categories = Category.objects.all()
        
        category = get_object_or_404(Category, pk=pk)
        
        product_list = Product.objects.filter(category_id__Category_ID__contains=pk)
        
        return render(request,'category.html', {'category' : category, 'product_list' : product_list, 'cart_item_count' : cart_item_count, 'categories' : categories})
    

class Search:

        def show_searched_products(request):
            
            cart_item_count = Cart.objects.filter(Customer_ID=request.user.id).count()
            categories = Category.objects.all()
                        
            if request.method == "GET":
                query = request.GET.get('search')
                
                if query == '':
                    query = 'None'
                    
                result = Product.objects.filter(Q(product_name__icontains=query) | Q(product_description__icontains=query))
                
                return render(request, 'search.html', {'query' : query, 'result' : result, 'cart_item_count' : cart_item_count, 'categories' : categories})
            
           
class Cart_View:

    def show_cart(request):
        
        categories = Category.objects.all()
        cart_item_count = Cart.objects.filter(Customer_ID=request.user.id).count()

        cart_items = Cart.objects.filter(Customer_ID = request.user.id)
        

        payment_sum = 0
                
        product = []
        
        for cart_item in cart_items:
           
            product.append([cart_item.cart_amount, Product.objects.get(Product_ID__contains = cart_item.product_key.Product_ID)])
            payment_sum += Product.objects.get(Product_ID__contains = cart_item.product_key.Product_ID).price * cart_item.cart_amount
        
        
        

        return render(request, 'cart.html', {'product': product, 'cart_item_count' : cart_item_count, 'payment_sum' : payment_sum, 'categories' : categories})
    
    def increase_cart_amount(request, pk):
        
        changing_item = Cart.objects.get(Customer_ID = request.user.id, product_key = pk)
        changing_item.cart_amount +=1        
        changing_item.save()
        
        return redirect('cart')
    
    
    def decrease_cart_amount(request, pk):
        
        changing_item = Cart.objects.get(Customer_ID = request.user.id, product_key = pk)
        
        if changing_item.cart_amount == 1:
            changing_item.cart_amount = 1
        else:
            changing_item.cart_amount -= 1
        changing_item.save()
        
        return redirect('cart')
    
    def change_cart_amount(request, pk):
        
        if request.method == 'GET':
            new_amount = request.GET.get('change_amount')
        
        changing_item = Cart.objects.get(Customer_ID = request.user.id, product_key = pk)
        
        if int(new_amount) > 0:
            changing_item.cart_amount = int(new_amount)
        
        changing_item.save()
        
        return redirect('cart')
    
    def delete_from_cart(request, pk):
        
        delete_obj = Cart.objects.get(Customer_ID=request.user.id, product_key=pk)
        delete_obj.delete()
        
        return redirect('cart')
    


class About_Us:

    def show_abouts(request):
        
        cart_item_count = Cart.objects.filter(Customer_ID=request.user.id).count()
        categories = Category.objects.all()

        return render(request, 'about_us.html', {'cart_item_count' : cart_item_count, 'categories' : categories})


class Imprint:

    def show_imprint(request):
        
        cart_item_count = Cart.objects.filter(Customer_ID=request.user.id).count()
        categories = Category.objects.all()

        return render(request, 'imprint.html', {'cart_item_count' : cart_item_count, 'categories' : categories})

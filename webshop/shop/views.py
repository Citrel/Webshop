from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from .forms import *
from django.db.models import Q, Sum, Count
from django import template
from profiles.models import *
from profiles.forms import *



class Homepage:

    def show_products(request):
        
        
        products = Product.objects.all()
        
        bestseller = Product.objects.filter(Selected = True)
        
        categories_with_items = []
        
        categories = Category.objects.all()
        cart_item_count = Cart.objects.filter(Customer_ID=request.user.id).count()
        
        for category in categories:
            
            product_items = Product.objects.filter(category_id = category.Category_ID)
            
            categories_with_items.append([category, product_items])
        
        
        return render (request, 'index.html', {'bestseller' : bestseller, 'products' : products, 'categories' : categories, 'cart_item_count' : cart_item_count,
                                                      'categories_with_items' : categories_with_items, 'product_items' : product_items})
        
        
    def show_liked_products(request):
        
        categories = Category.objects.all()
        cart_item_count = Cart.objects.filter(Customer_ID=request.user.id).count()
        
        liked_products = []
        user_likes = Product_Likes.objects.filter(Customer_ID = request.user.id)
        for user_like in user_likes:
            liked_products.append([Product.objects.get(Product_ID = user_like.Product_ID.Product_ID)])
        
        return render(request, 'liked_products.html', {'cart_item_count' : cart_item_count, 'categories' : categories, 'liked_products' : liked_products})
    
    def show_order_history(request):
        
        categories = Category.objects.all()
        cart_item_count = Cart.objects.filter(Customer_ID=request.user.id).count()
        
        your_orders = Order.objects.filter(user = request.user.id)
        orders_with_products = []
        
        for your_order in your_orders:
            
            order_products = Products_per_Order.objects.filter(Order_ID = your_order.Order_ID)
            orders_with_products.append(your_order, order_products)
        
        
        
        return render(request, 'order_history.html', {'cart_item_count' : cart_item_count, 'categories' : categories})
        
        
    
    

class Article():
    
    def show_information(request, pk):
        
        cart_item_count = Cart.objects.filter(Customer_ID=request.user.id).count()
        categories = Category.objects.all()
        
        product = get_object_or_404(Product, pk=pk)
        likes = Product_Likes.objects.filter(Product_ID = pk).count() 
        likedProduct = Product.objects.get(Product_ID = pk)
        is_liked = False
        
        if request.user.is_authenticated:
            created = Product_Likes.objects.filter(Customer_ID_id= request.user.id, Product_ID = likedProduct).exists()
            if not created:
                is_liked = False
            else:
                is_liked = True
            
        
        return render(request, 'product_detail.html',{'product' : product, 'likes' : likes, 'is_liked' : is_liked , 'cart_item_count' : cart_item_count, 'categories' : categories})
    
    def like_product(request, pk):
        
        
        if request.method == 'POST':
            likedProduct = Product.objects.get(Product_ID = pk)
        
            liked, created = Product_Likes.objects.get_or_create(defaults={'Product_ID': likedProduct}, Customer_ID_id= request.user.id, Product_ID = likedProduct)
        
        
            if not created:
                liked.delete()
            else:
                liked.save()
            
        
            return redirect('details', pk = pk)
        return render(request,'product_detail.html')
    
    
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
           

            product_id = cart_item.product_key.Product_ID
            product.append([cart_item.cart_amount, Product.objects.get(Product_ID= product_id), 
                            Product.objects.get(Product_ID = product_id).price * cart_item.cart_amount])
            payment_sum += Product.objects.get(Product_ID = product_id).price * cart_item.cart_amount
        
        

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
        
        if request.method == 'POST':
            new_amount = request.POST.get('change_amount')
        
        changing_item = Cart.objects.get(Customer_ID = request.user.id, product_key = pk)
        
        if int(new_amount) > 0:
            changing_item.cart_amount = int(new_amount)
        
        changing_item.save()
        
        return redirect('cart')
    
    def delete_from_cart(request, pk):
        
        delete_obj = Cart.objects.get(Customer_ID=request.user.id, product_key=pk)
        delete_obj.delete()
        
        return redirect('cart')
    
    
class Order_Views:
    
    def show_process_order(request):
        
        categories = Category.objects.all()
        cart_item_count = Cart.objects.filter(Customer_ID=request.user.id).count()

        delivery_address = get_object_or_404(User_Delivery_Address, user=request.user)
        payment_address = get_object_or_404(User_Payment_Address, user=request.user)
        credit_card = get_object_or_404(User_Credit_Card, user=request.user)
        paypal = get_object_or_404(User_PayPal, user=request.user)
        debit = get_object_or_404(User_Debit, user=request.user)
        if request.method == 'POST':
            user_delivery_address_form = User_Delivery_AddressForm(request.POST, instance=delivery_address)
            user_payment_address_form = User_Payment_AddressForm(request.POST, instance=payment_address)
            user_credit_card_form = User_Credit_CardForm(request.POST, instance=credit_card)
            user_paypal_form = User_PayPalForm(request.POST, instance=paypal)
            user_debit_form = User_DebitForm(request.POST, instance=debit)
        if profile_form.is_valid() and user_delivery_address_form.is_valid() and user_payment_address_form.is_valid() and user_credit_card_form.is_valid() and user_paypal_form.is_valid() and user_debit_form.is_valid():
            profile_form.save()
            user_delivery_address_form.save()
            user_payment_address_form.save()
            user_credit_card_form.save()
            user_paypal_form.save()
            user_debit_form.save()
            messages.success(request, 'Daten wurden aktualisiert')
            return redirect('order')
        else:
            profile_form = ProfileForm(instance=request.user)
            user_delivery_address_form = User_Delivery_AddressForm(instance=delivery_address)
            user_payment_address_form = User_Payment_AddressForm(instance=payment_address)
            user_credit_card_form = User_Credit_CardForm(instance=credit_card)
            user_paypal_form = User_PayPalForm(instance=paypal)
            user_debit_form = User_DebitForm(instance=debit)
        
        order_items = Cart.objects.filter(Customer_ID = request.user.id)
        product = []
        payment_sum = 0
        
        for order_item in order_items:

            product_id = order_item.product_key.Product_ID
            product.append([order_item.cart_amount, Product.objects.get(Product_ID= product_id), 
                            Product.objects.get(Product_ID = product_id).price * order_item.cart_amount])
            payment_sum += Product.objects.get(Product_ID = product_id).price * order_item.cart_amount
            
        context = {
            'product' : product,
            'payment_sum' : payment_sum,
            'categories' : categories,
            'cart_item_count' : cart_item_count,
            'profile_form': profile_form,
            'user_delivery_address_form': user_delivery_address_form,
            'user_payment_address_form': user_payment_address_form,
            'user_credit_card_form': user_credit_card_form,
            'user_paypal_form': user_paypal_form,
            'user_debit_form': user_debit_form
            }
            
        return render(request, 'process_order.html', context)
    
    
    def show_payment_info(request):
        
        your_credit_card = User_Credit_Card.objects.get(user = request.user.id)
        
        your_debit_card = User_Debit.objects.get(user = request.user.id)
        
        your_paypal = User_PayPal.objects.get(user = request.user.id)
        
        categories = Category.objects.all()
        cart_item_count = Cart.objects.filter(Customer_ID=request.user.id).count()
        
        return render(request,'process_payment_information.html' , {'cart_item_count' : cart_item_count, 'categories' : categories,  'your_credit_card' : your_credit_card, 'your_debit_card' : your_debit_card, 'your_paypal' : your_paypal})
        
        
    
    def choose_payment_info(request, pk):
        
        your_credit_card = User_Credit_Card.objects.get(user = request.user.id)
        
        your_debit_card = User_Debit.objects.get(user = request.user.id)
        
        your_paypal = User_PayPal.objects.get(user = request.user.id)
        
        if Payment_Method.objects.filter(user = request.user.id).exists() == True:
            
            if pk == your_credit_card.id:
                credit_payment = Payment_Method.objects.get(user = request.user.id)
                credit_payment.method_name = 'Kredit Karte'
                credit_payment.method_fee = 0.02
            
            elif pk == your_debit_card.id:
                debit_payment = Payment_Method.objects.get(user = request.user.id)
                debit_payment.method_name = 'Lastschrift'
                debit_payment.method_fee = 0.02
        
            elif pk == your_paypal.id:
                paypal_payment = Payment_Method.objects.get(user = request.user.id)
                paypal_payment.method_name = 'Paypal'
                paypal_payment.method_fee = 0.0249
            
        else:
            
            if pk == your_credit_card.id:
                credit_payment = Payment_Method.objects.create(method_name = 'Kredit Karte', method_fee = 0.02, user = request.user.id)
                credit_payment.save()
            
            elif pk == your_debit_card.id:
                debit_payment = Payment_Method.objects.create(method_name = 'Lastschrift', method_fee = 0.02, user = request.user.id)
                debit_payment.save()
        
            elif pk == your_paypal.id:
                paypal_payment = Payment_Method.objects.create(method_name = 'Paypal', method_fee = 0.0249, user = request.user.id)
                paypal_payment.save()
        
            
        return redirect('order_information')
    
    
    def checkout(request):
        
        categories = Category.objects.all()
        cart_item_count = Cart.objects.filter(Customer_ID=request.user.id).count()
        
        payment_info = Payment_Method.objects.get(user = request.user.id)
        delivery_adress = User_Delivery_Address.objects.get(user = request.user.id)
        payment_adress = User_Payment_Address.objects.get(user = request.user.id)
        
        new_order = Order.objects.create(user = request.user.id, payment_method_id = payment_info.Payment_Method_ID,payment_adress_id = payment_adress.id , payed = False, delivery = delivery_adress.id)
        new_order.save()
        
        order_items = Cart.objects.filter(Customer_ID = request.user.id)
        
        for order_item in order_items:

            new_entry = Products_per_Order.objects.create(Order_ID = new_order.Order_ID, Product_ID = order_item.product_key, order_amount = order_item.cart_amount, product_price_at_order_time = order_item.product_key.price)
            new_entry.save
            
        order_items.delete()
        
        return render(request, 'order_complete.html', {'cart_item_count' : cart_item_count, 'categories' : categories})
        
        
class About_Us:

    def show_abouts(request):
        
        cart_item_count = Cart.objects.filter(Customer_ID=request.user.id).count()
        categories = Category.objects.all()

        return render(request, 'about_us.html', {'cart_item_count' : cart_item_count, 'categories' : categories})

class AGB:
    
    def show_agbs(request):
        
        cart_item_count = Cart.objects.filter(Customer_ID=request.user.id).count()
        categories = Category.objects.all()

        return render(request, 'AGBs.html', {'cart_item_count' : cart_item_count, 'categories' : categories})


class Imprint:

    def show_imprint(request):
        
        cart_item_count = Cart.objects.filter(Customer_ID=request.user.id).count()
        categories = Category.objects.all()

        return render(request, 'imprint.html', {'cart_item_count' : cart_item_count, 'categories' : categories})

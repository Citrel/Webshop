"""webshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
    Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from shop import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Homepage.show_products, name='index'),
    path('search', views.Search.show_searched_products, name="searching"),
    path('liked', views.Homepage.show_liked_products, name='products_liked'), 
    path('details/<slug:pk>', views.Article.show_information, name='details'),
    path('details/<slug:pk>/like', views.Article.like_product, name='like'),
    path('details/<slug:pk>/add_to_cart', views.Article.add_to_cart, name = 'add_to_cart'),
    path('categories/<slug:pk>', views.Categories.show_categories, name='categories'),
    path('order', views.Order_Views.show_process_order, name = 'order'),
    path('about_us', views.About_Us.show_abouts, name='about_us'),
    path('imprint', views.Imprint.show_imprint, name='imprint'),
    path('cart', views.Cart_View.show_cart, name = 'cart'),
    path('AGB', views.AGB.show_agbs, name = 'AGB'),
    path('cart/<slug:pk>/increase', views.Cart_View.increase_cart_amount, name='increase'),
    path('cart/<slug:pk>/decrease', views.Cart_View.decrease_cart_amount, name='decrease'),
    path('cart/<slug:pk>/change', views.Cart_View.change_cart_amount, name='change'),
    path('cart/<slug:pk>/delete', views.Cart_View.delete_from_cart, name='delete'),
    path('profiles/', include('profiles.urls'))
]

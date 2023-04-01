from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.Profiles.register, name='register'),
    path('login/', views.Profiles.login, name='login'),
    path('logout/', views.Profiles.logout, name='logout'),
    path('myprofile/', views.Profiles.myprofile, name='myprofile'),
    path('', views.Profiles.myprofile, name='myprofile'),

    path('activate/<uidb64>/<token>/', views.Profiles.activate, name='activate'),
    path('forgot_password/', views.Profiles.forgot_password, name='forgot_password'),
    path('reset_password_validate/<uidb64>/<token>/',
         views.Profiles.reset_password_validate, name='reset_password_validate'),
    path('reset_password', views.Profiles.reset_password, name='reset_password'),
]

from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Profile
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Profile.objects.create_user(
                first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()
            messages.success(request, 'Registrierung erfolgreich')
            return redirect('register')
    else:
        form = RegistrationForm()
    return render(request, 'profiles/register.html', context={'form': form})


def login(request):
    return render(request, 'profiles/login.html')


def logout(request):
    return

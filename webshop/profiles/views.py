from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Profile
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# VERIFICATION
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


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
            # USER ACTIVATION EMAIL
            current_site = get_current_site(request)
            mail_subject = 'Konto Aktivieren'
            message = render_to_string('profiles/profile_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            return redirect('/profiles/login/?command=verification&email='+email)
    else:
        form = RegistrationForm()
    return render(request, 'profiles/register.html', context={'form': form})


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Du bist jetzt angemeldet.')
            return redirect('myprofile')
        else:
            messages.error(request, 'Email oder Passwort ist falsch!')
            return redirect('login')
    return render(request, 'profiles/login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'Du bist jetzt abgemeldet.')
    return redirect('login')


@login_required(login_url='login')
def myprofile(request):
    return render(request, 'profiles/myprofile.html')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Profile._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Profile.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Profil erfolgreich aktiviert.')
        return redirect('login')
    else:
        messages.error(request, 'Ungültiger Aktivierungslink.')
        return redirect('register')


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Profile.objects.filter(email=email).exists():
            user = Profile.objects.get(email__exact=email)
            # RESET PASSWORD EMAIL
            current_site = get_current_site(request)
            mail_subject = 'Passwort zurücksetzen'
            message = render_to_string('profiles/reset_password_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            messages.success(request, 'Email wurde versendet.')
            return redirect('login')
        else:
            messages.error(request, 'Du hast noch kein Profil')
            return redirect('forgot_password')
    return render(request, 'profiles/forgot_password.html')


def reset_password_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Profile._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Profile.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Bitte neues Passwort eingeben.')
        return redirect('reset_password')
    else:
        messages.error(request, 'Der ist nicht mehr gültig.')
        return redirect('login')


def reset_password(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['condirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Profile.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Passwort wurde zurückgesetzt.')
        else:
            messages.error(request, 'Passwörter sind nicht identisch.')
            return redirect('reset_password')
    else:
        return render(request, 'profiles/reset_password.html')

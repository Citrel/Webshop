from django import forms

class LoginForm(forms.Form):
    email = forms.EmailInput(label="Email Addresse")
    password = forms.PasswordInput(label="Passwort")

class RegisterForm(forms.Form):
    vorname = forms.CharField(label="Vorname", max_length=100)
    nachname = forms.CharField(label="Nachname", max_length=100)
    email = forms.EmailInput(label="Email Addresse")
    password = forms.PasswordInput(label="Passwort")
    repeated_password = forms.PasswordInput(label="Wiederhole das Passwort")

class SearchForm(forms.Form):
    searched_word = forms.TextInput(attrs="style='width:60%;' placeholder='Suchen'")
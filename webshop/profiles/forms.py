from django import forms
from .models import Profile, User_Delivery_Address, User_Payment_Address, User_Credit_Card, User_PayPal, User_Debit


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Passwort eingeben',
        'class': 'form-control',
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Passwort wiederholen',
        'class': 'form-control'
    }))

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name',
                  'phone_number', 'email', 'password']

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Passwörter sind nicht identisch!"
            )

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'phone_number')

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class User_Delivery_AddressForm(forms.ModelForm):
    class Meta:
        model = User_Delivery_Address
        fields = ('delivery_street', 'delivery_house_number',
                  'delivery_city', 'delivery_plz')

    def __init__(self, *args, **kwargs):
        super(User_Delivery_AddressForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class User_Payment_AddressForm(forms.ModelForm):
    class Meta:
        model = User_Payment_Address
        fields = ('payment_street', 'payment_house_number',
                  'payment_city', 'payment_plz')

    def __init__(self, *args, **kwargs):
        super(User_Payment_AddressForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class User_Credit_CardForm(forms.ModelForm):
    class Meta:
        model = User_Credit_Card
        fields = ('owner_first_name', 'owner_last_name', 'card_number',
                  'expiration_date_month', 'expiration_date_year', 'security_code')

    def __init__(self, *args, **kwargs):
        super(User_Credit_CardForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class User_PayPalForm(forms.ModelForm):
    class Meta:
        model = User_PayPal
        fields = ('paypal_mail', 'paypal_password')

    def __init__(self, *args, **kwargs):
        super(User_PayPalForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class User_DebitForm(forms.ModelForm):
    class Meta:
        model = User_Debit
        fields = ('debit_first_name', 'debit_last_name', 'iban', 'bic')

    def __init__(self, *args, **kwargs):
        super(User_DebitForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

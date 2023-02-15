from django import forms


class Search_Form(forms.Form):
    searched_word = forms.TextInput(
        attrs={'style': 'width:60%;', 'placeholder': 'Suchen'})


class Change_Password_Form(forms.Form):
    old_password = forms.PasswordInput(label="Altes Passwort")
    new_password = forms.PasswordInput(label="Neues Passwort")


class Creditcard_Payment_Form(forms.Form):
    creditcard_number = forms.TextInput(label="Nummer: ", attrs={
                                        'placeholder': '{{ creditcard_information.credit_card_number }}'})
    creditcard_expiration_date = forms.TextInput(label="Ablaufdatum: ", attrs={
                                                 'placeholder': '{{ creditcard_information.expiration_date }}'})


class Paypal_Payment_Form(forms.Form):
    paypal_email = forms.TextInput(label="Email: ", attrs={
                                   'placeholder': ' {{ paypal_information.email }} '})


class Debitcard_Payment_Form(forms.Form):
    debitcard_number = forms.TextInput(label="Nummer: ", attrs={
                                       'placeholder': ' {{ debitcard_information.debitcard_number }} '})


class Billing_Address_Form(forms.Form):
    billing_address_plz = forms.TextInput(label="Postleitzahl", attrs={
                                          'placeholder': ' {{ billing_address.plz }} '})
    billing_address_city = forms.TextInput(
        label="Stadt", attrs={'placeholder': ' {{ billing_address.city }} '})
    billing_address_street = forms.TextInput(
        label="Straßenname", attrs={'placeholder': ' {{ billing_address.street }} '})
    billing_address_house_number = forms.TextInput(label="Hausnummer", attrs={
                                                   'placeholder': ' {{ billing_address.house_number }} '})


class Payment_Address_Form(forms.Form):
    payment_address_plz = forms.TextInput(label="Postleitzahl", attrs={
                                          'placeholder': ' {{ payment_address.plz }} '})
    payment_address_city = forms.TextInput(
        label="Stadt", attrs={'placeholder': ' {{ payment_address.city }} '})
    payment_address_street = forms.TextInput(
        label="Straßenname", attrs={'placeholder': ' {{ payment_address.street }} '})
    payment_address_house_number = forms.TextInput(label="Hausnummer", attrs={
                                                   'placeholder': ' {{ payment_address.house_number }} '})

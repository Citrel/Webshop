from django import forms


class Search_Form(forms.Form):
    searched_word = forms.TextInput(
        attrs={'style': 'width:60%;', 'placeholder': 'Suchen'})


class Change_Password_Form(forms.Form):
    old_password = forms.PasswordInput()
    new_password = forms.PasswordInput()

from django import forms


class SignUpForm(forms.Form):

    name = forms.CharField(max_length=20, required=False)
    email = forms.CharField(max_length=20, required=False)
    password = forms.CharField(max_length=20, required=False)

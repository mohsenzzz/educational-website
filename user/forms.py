from django import forms
from phonenumber_field.formfields import PhoneNumberField
from pyexpat.errors import messages

from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('phone_number','username')
    # phone_number = PhoneNumberField(widget=forms.TextInput(attrs={''}), required=True)
    phone_number = PhoneNumberField(region='IR',
        widget=forms.TextInput(
        attrs={'placeholder': ' phone number'}),
        required=True

    )
    username = forms.CharField(required=True)
    # class Meta:
    #     model = User
    #     fields = ('username', 'first_name','last_name','phone_number', 'password')
    #     widgets = {
    #       'password': PasswordInput({
    #           'class': 'form-control',
    #           'placeholder': 'Password',
    #
    #       }),
    #         'phone_number': NumberInput({
    #             'class': 'form-control',
    #             'placeholder': 'Phone Number',
    #         })
    #     }


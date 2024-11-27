from django import forms
from phonenumber_field.formfields import PhoneNumberField
from pyexpat.errors import messages

from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('phone_number','username', 'password')
    # phone_number = PhoneNumberField(widget=forms.TextInput(attrs={''}), required=True)
    phone_number = PhoneNumberField(region='IR',
        widget=forms.TextInput(
        attrs={'placeholder': ' phone number'}),
        required=True

    )
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user



class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)



class UpdateForm(forms.Form):
    class Meta:
        model = User
        fields = ('first_name','last_name', 'username')

    username = forms.CharField(required=True)

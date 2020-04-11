from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import BusinessInfo

class UserRegisterForm(UserCreationForm):
    """ Form to register a new user to User table """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    """ Form to update User info username and email """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class BusinessRegisterForm(forms.ModelForm):
    """ 
    Form to collect basic business information 
    from potential business customer
    """
    class Meta:
        model = BusinessInfo
        fields = ['business_name', 'kvk_num']

class BusinessProfileForm(forms.ModelForm):
    """ 
    Form to add full business profile to database
    """
    class Meta:
        model = BusinessInfo
        fields = [
            'business_name',
            'website',
            'phone',
            'street_name',
            'street_num',
            'postcode',
            'town',
            'facebook',
            'instagram',
            'twitter'
        ]
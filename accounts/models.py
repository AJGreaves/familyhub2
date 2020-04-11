from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField

# Create your models here.
class BusinessInfo(models.Model):
    """ Model for Users Business Information """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=25)
    kvk_num = models.CharField(max_length=20)
    # logo = image
    website = models.SlugField(max_length=50)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    street_name = models.CharField(max_length=50)
    street_num = models.CharField(max_length=10)
    postcode = models.CharField(max_length=10)
    town = models.CharField(max_length=25)
    facebook = models.SlugField(blank=True, max_length=100)
    instagram = models.SlugField(blank=True, max_length=100)
    twitter = models.SlugField(blank=True, max_length=100)
    foundation = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)

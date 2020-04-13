from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Application(models.Model):
    """
    Model to store applications to advertise with FamilyHub.
    Code for phone number and regex taken from
    https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
    """
    AWAITING = 'Awaiting response'
    APPROVED = 'Approved'
    DENIED = 'Denied'
    STATUS_CHOICES = [
        (AWAITING, 'Awaiting response'),
        (APPROVED, 'Approved'),
        (DENIED, 'Denied'),
    ] 
    contact_name = models.CharField(max_length=25)
    business_name = models.CharField(max_length=25)
    kvk_num = models.CharField(max_length=20)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    message = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=AWAITING,
    )

    def __str__(self):
        return f'{self.business_name}: {self.status}'

# Create your models here.
class BusinessInfo(models.Model):
    """ Model for Users Business Information """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=25)
    kvk_num = models.CharField(max_length=20)
    # logo = image
    website = models.SlugField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    street_name = models.CharField(max_length=50)
    street_num = models.CharField(max_length=10)
    postcode = models.CharField(max_length=10)
    town = models.CharField(max_length=25)
    facebook = models.SlugField(blank=True, max_length=100)
    instagram = models.SlugField(blank=True, max_length=100)
    twitter = models.SlugField(blank=True, max_length=100)
    foundation = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)

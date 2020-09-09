from django.db import models
from django.core.validators import RegexValidator

class Customer(models.Model):
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)
    
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, verbose_name='email address', max_length=255)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    
    REQUIRED_FIELDS = ['email', 'last_name']
    
    class Meta:
        ordering = ['created']


class Reservation(models.Model):
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)
    
    name = models.CharField(max_length=200)
    reservation_date = models.DateTimeField('date reservation')
    address = models.CharField(max_length=500, blank=True)
    
    class Meta:
        ordering = ['created']

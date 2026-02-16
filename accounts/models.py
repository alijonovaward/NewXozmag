from django.contrib.auth.models import User
from django.db import models
from shops.models import Shop

# Create your models here.
class Profile(models.Model):
    USER_TYPES = (
        ('superadmin', 'Superadmin'),
        ('owner', 'Owner'),
        ('employee', 'Employee'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone_number = models.CharField(max_length=11)
    location = models.CharField(max_length=100)
    user_type = models.CharField(max_length=100, choices=USER_TYPES)

    is_deleted = models.BooleanField(default=False)

    shop = models.ForeignKey(
        'shops.Shop',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='employees'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
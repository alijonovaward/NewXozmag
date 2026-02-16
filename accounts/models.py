from django.contrib.auth.models import User
from django.db import models

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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
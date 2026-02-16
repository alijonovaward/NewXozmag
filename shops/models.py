from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    owner = models.ForeignKey(User, related_name='shops',
                              on_delete=models.CASCADE,
                              limit_choices_to={'profile__user_type': 'owner'})
    employee = models.ManyToManyField(User, related_name='employee_shops',blank=True,
                                   limit_choices_to={'profile__user_type': 'employee'})

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

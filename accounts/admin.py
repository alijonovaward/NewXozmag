from django.contrib import admin
from .models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'location', 'user_type', 'created_at', 'updated_at')
    list_filter = ('user_type', 'created_at', 'updated_at')
    search_fields = ('user', 'phone_number', 'location')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

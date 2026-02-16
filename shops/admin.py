from django.contrib import admin
from .models import Shop

# Register your models here.
@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location','owner', 'created_at', 'updated_at')
    search_fields = ('name', 'location')
    list_filter = ('owner',)
    ordering = ('-created_at',)
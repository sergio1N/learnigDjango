from django.contrib import admin

# Register your models here.
from .models import Menu, Menu_category

admin.site.register(Menu)
admin.site.register(Menu_category)
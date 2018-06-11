from django.contrib import admin
from .models import MenuItem
# Register your models here.


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    fields = ('menu', 'parent', 'title')
    list_display = ('__str__', )
    list_filter = ('level', )
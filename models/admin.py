from django.contrib import admin
from .models import *

admin.site.register([Service_Model, Service_Section_Model])


@admin.register(Contact_Model)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'called']

from django.contrib import admin
from .models import *
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.detail import DetailView

@admin.register(Contact_Model)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'called']

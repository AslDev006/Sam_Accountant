from django.contrib import admin
from .models import *

admin.site.register([Service_Model, Service_Section_Model, Contact_Model])
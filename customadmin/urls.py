from django.urls import path
from .views import *

urlpatterns =[
    path('', admin_login, name="admin_login"),
    path('dashboard/', admin_dashboard, name="admin_dashboard"),
    path('contact/', contact, name="admin_contact"),
    path('called/', called, name="called"),
    path('uncalled-contact/', Uncalled, name="uncalled"),
    path('uncalled-contact/<id>/', single_contact, name="single"),
]
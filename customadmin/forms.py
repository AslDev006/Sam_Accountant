from django import forms
from models.models import Contact_Model


# creating a form
class ContactForm(forms.ModelForm):
    # create meta class
    class Meta:
        model = Contact_Model
        fields = ["called"]
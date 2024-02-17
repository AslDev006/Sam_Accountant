import uuid
from django.db import models

class Service_Model(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=350)
    objects = models.Manager()
    def __str__(self):
        return self.name

class Service_Section_Model(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sections = models.ForeignKey(Service_Model, related_name='sections', on_delete=models.CASCADE)
    name = models.TextField()
    objects = models.Manager()
    def __str__(self):
        return self.name


class Contact_Model(models.Model):
    class Call_type(models.TextChoices):
        Boglanildi = "Bog'lanildi"
        Boglanilmadi = "Bog'lanilmadi"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=13)
    called = models.CharField(max_length=100, choices=Call_type, default=Call_type.Boglanilmadi)
    def __str__(self):
        return self.name

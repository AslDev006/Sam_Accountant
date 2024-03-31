# Generated by Django 5.0.2 on 2024-03-31 07:47

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Model',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=13)),
                ('called', models.CharField(choices=[("Bog'lanildi", 'Boglanildi'), ("Bog'lanilmadi", 'Boglanilmadi')], default="Bog'lanilmadi", max_length=100)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service_Model',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='Service_Section_Model',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('sections', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='models.service_model')),
            ],
        ),
    ]

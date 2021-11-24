# Generated by Django 3.2.9 on 2021-11-23 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_state', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental_state',
            name='property_type',
            field=models.CharField(choices=[('AP', 'APARTAMENTO'), ('C', 'CASA'), ('CC', 'CASA DE CONDOMÍNIO'), ('CO', 'COBERTURA'), ('FL', 'FLAT'), ('SO', 'SOBRADO')], default='AP', max_length=2),
        ),
    ]

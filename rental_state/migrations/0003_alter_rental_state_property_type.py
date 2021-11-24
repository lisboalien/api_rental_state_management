# Generated by Django 3.2.9 on 2021-11-23 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_state', '0002_alter_rental_state_property_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental_state',
            name='property_type',
            field=models.CharField(choices=[('AP', 'APARTAMENTO'), ('C', 'CASA'), ('CC', 'CASA DE CONDOMÍNIO'), ('CO', 'COBERTURA'), ('FL', 'FLAT'), ('SO', 'SOBRADO')], default='AP', max_length=3),
        ),
    ]

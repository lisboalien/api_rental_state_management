# Generated by Django 3.2.9 on 2021-11-23 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_state', '0006_alter_rental_state_property_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental_state',
            name='property_type',
            field=models.CharField(max_length=2),
        ),
    ]
# Generated by Django 5.0.2 on 2024-02-24 19:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_coffeebean_roast_date_alter_coffeebean_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeebean',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]

# Generated by Django 2.0.7 on 2020-06-06 17:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plates', '0006_auto_20180715_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='plate',
            name='accuracy',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plate',
            name='detector',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='plate',
            name='license_number',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]{3}[0-9]{3}$', 'Wrong format. Please use ABC123 format.')]),
        ),
    ]

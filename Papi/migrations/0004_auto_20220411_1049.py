# Generated by Django 2.2.12 on 2022-04-11 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Papi', '0003_auto_20220411_1044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='status',
            new_name='payment',
        ),
    ]

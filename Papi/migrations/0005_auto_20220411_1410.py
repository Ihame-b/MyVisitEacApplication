# Generated by Django 2.2.12 on 2022-04-11 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Papi', '0004_auto_20220411_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='product_image'),
        ),
    ]

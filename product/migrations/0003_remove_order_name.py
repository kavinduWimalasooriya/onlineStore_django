# Generated by Django 3.2.4 on 2021-06-21 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
    ]

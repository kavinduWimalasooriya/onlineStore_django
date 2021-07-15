# Generated by Django 3.2.4 on 2021-06-21 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_order_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='number_of_orders',
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]

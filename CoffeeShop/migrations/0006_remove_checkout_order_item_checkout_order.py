# Generated by Django 4.2.1 on 2023-06-28 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeShop', '0005_remove_checkout_order_checkout_order_item_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='order_item',
        ),
        migrations.AddField(
            model_name='checkout',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CoffeeShop.order'),
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-28 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeShop', '0004_remove_orderitem_coffees_orderitem_coffees'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='order',
        ),
        migrations.AddField(
            model_name='checkout',
            name='order_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CoffeeShop.orderitem'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products/'),
        ),
    ]

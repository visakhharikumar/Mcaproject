# Generated by Django 2.2 on 2019-05-16 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_order_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('order placed', 'ORDER PLACED'), ('dispatched', 'DISPATCHED'), ('delivered', 'DELIVERED'), ('cancelled', 'CANCELLED'), ('returned', 'RETURNED')], default='Order Placed', max_length=50),
        ),
    ]

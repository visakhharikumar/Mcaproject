# Generated by Django 2.2 on 2019-04-27 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_orderdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_id',
        ),
    ]

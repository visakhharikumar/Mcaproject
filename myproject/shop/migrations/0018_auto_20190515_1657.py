# Generated by Django 2.2 on 2019-05-15 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20190515_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='status_text',
            field=models.CharField(default='Order Placed', max_length=50),
        ),
    ]

# Generated by Django 2.2 on 2019-04-06 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20190406_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(default='shop/static/images/home/gallery2.jpg', upload_to='shop/static/images/home/'),
        ),
    ]
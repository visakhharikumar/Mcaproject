# Generated by Django 2.2 on 2019-05-15 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_order_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_text', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.OrderStatus'),
        ),
    ]

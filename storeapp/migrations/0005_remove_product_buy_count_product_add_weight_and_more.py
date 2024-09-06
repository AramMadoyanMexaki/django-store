# Generated by Django 4.2.11 on 2024-09-06 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0004_alter_product_price_storeuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='buy_count',
        ),
        migrations.AddField(
            model_name='product',
            name='add_weight',
            field=models.FloatField(default=1.0, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='buy_weight',
            field=models.FloatField(default=0),
        ),
        migrations.DeleteModel(
            name='StoreUser',
        ),
    ]

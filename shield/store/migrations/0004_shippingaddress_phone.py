# Generated by Django 4.0 on 2022-04-24 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='phone',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]

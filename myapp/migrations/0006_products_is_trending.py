# Generated by Django 3.2.1 on 2021-05-17 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_products_discounted_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='is_trending',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 3.2.1 on 2021-06-15 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_auto_20210615_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout_cart',
            name='name',
        ),
    ]

# Generated by Django 3.2.1 on 2021-06-18 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_auto_20210618_2030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order',
            new_name='address',
        ),
    ]

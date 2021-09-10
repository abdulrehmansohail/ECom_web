# Generated by Django 3.2.1 on 2021-06-21 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_auto_20210618_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complete_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.address')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.cart')),
            ],
        ),
        migrations.CreateModel(
            name='Order_Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.cart')),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]

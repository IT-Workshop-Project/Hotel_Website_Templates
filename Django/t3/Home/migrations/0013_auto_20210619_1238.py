# Generated by Django 3.2.3 on 2021-06-19 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_auto_20210619_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='checkin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='checkout',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='hotelmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

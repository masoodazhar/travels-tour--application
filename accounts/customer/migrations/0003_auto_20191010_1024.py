# Generated by Django 2.2.4 on 2019-10-10 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customerinstallment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerinstallment',
            name='customerid',
            field=models.CharField(max_length=50),
        ),
    ]
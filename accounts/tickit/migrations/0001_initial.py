# Generated by Django 2.2.4 on 2019-10-09 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50)),
                ('pticketno', models.CharField(max_length=50)),
                ('pamount', models.CharField(max_length=50)),
                ('pnrfrom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateofissue', models.DateField()),
                ('root', models.CharField(max_length=50)),
                ('traveldate', models.DateField()),
                ('pnr', models.CharField(max_length=50)),
                ('totalamount', models.IntegerField()),
                ('recievedamount', models.IntegerField()),
                ('recieveableamount', models.IntegerField()),
                ('remainingamount', models.IntegerField()),
                ('profit', models.IntegerField()),
                ('madeby', models.CharField(default='Mubeen', max_length=50)),
                ('Description', models.TextField(default=' ')),
                ('airline', models.ForeignKey(default='PIA', on_delete=django.db.models.deletion.CASCADE, to='tickit.Airline')),
                ('careof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
            ],
        ),
    ]

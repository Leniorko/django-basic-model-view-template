# Generated by Django 3.2.7 on 2021-09-24 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('surname', models.CharField(max_length=250)),
                ('current_car', models.CharField(max_length=250)),
                ('contact_number', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PastService',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basicapp.clients')),
            ],
        ),
    ]

# Generated by Django 4.0.2 on 2022-02-22 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicleNo', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=25)),
                ('model', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicleNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.vehicle')),
            ],
        ),
    ]

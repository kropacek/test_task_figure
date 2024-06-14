# Generated by Django 5.0.6 on 2024-06-14 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_number', models.CharField(choices=[('101', '101'), ('102', '102'), ('K103', 'K103')], max_length=8, unique=True)),
                ('model', models.CharField(choices=[('БЕЛАЗ', 'БЕЛАЗ'), ('Komatsu', 'Komatsu')], max_length=20)),
                ('max_load', models.FloatField()),
                ('current_load', models.FloatField()),
                ('unload_coordinates', models.CharField(blank=True, max_length=20, null=True)),
                ('fe_percentage', models.FloatField()),
                ('sio2_percentage', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('volume_before_unload', models.FloatField()),
                ('volume_after_unload', models.FloatField(blank=True, null=True)),
                ('sio2_percentage_before', models.FloatField()),
                ('fe_percentage_before', models.FloatField()),
                ('sio2_percentage_after', models.FloatField(blank=True, null=True)),
                ('fe_percentage_after', models.FloatField(blank=True, null=True)),
                ('polygon', models.CharField(max_length=100)),
            ],
        ),
    ]

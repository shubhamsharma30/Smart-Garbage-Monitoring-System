# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-30 05:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='C_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_Username', models.CharField(max_length=200)),
                ('C_Password', models.CharField(max_length=200)),
                ('C_Name', models.CharField(max_length=200)),
                ('C_Address', models.CharField(max_length=200)),
                ('C_Ph_no', models.CharField(max_length=11)),
                ('C_Dustbin_ID', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='D_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('D_Username', models.CharField(max_length=200)),
                ('D_Password', models.CharField(max_length=200)),
                ('D_Name', models.CharField(max_length=200)),
                ('D_Address', models.CharField(max_length=200)),
                ('D_Ph_no', models.CharField(max_length=11)),
                ('Truck_no', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Trashcan1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('T_ID', models.CharField(max_length=10)),
                ('T_x_c', models.CharField(max_length=14)),
                ('T_y_c', models.CharField(max_length=14)),
                ('T_C_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='login.C_Details')),
                ('T_D_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='login.D_Details')),
            ],
        ),
        migrations.AddField(
            model_name='c_details',
            name='C_D_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.D_Details'),
        ),
    ]

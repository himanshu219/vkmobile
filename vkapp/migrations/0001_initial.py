# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_number', models.CharField(help_text=b'Please enter 10 digit mobile number only.', unique=True, max_length=15, verbose_name=b'Mobile Number', validators=[django.core.validators.MaxLengthValidator(10), django.core.validators.MinLengthValidator(10), django.core.validators.validate_integer])),
                ('name', models.CharField(help_text=b'Edit the Name of the customer if incorrect', max_length=50, verbose_name=b'Customer Name', validators=[django.core.validators.MinLengthValidator(3)])),
                ('address', models.TextField(help_text=b'Address of the customer', null=True, blank=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('model_number', models.CharField(max_length=100)),
                ('model_name', models.CharField(max_length=100)),
                ('total_quantity', models.IntegerField(default=0)),
                ('available_quantity', models.IntegerField(default=0)),
                ('selling_price', models.DecimalField(default=0.0, max_digits=11, decimal_places=8)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductSales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=0)),
                ('product', models.ForeignKey(to='vkapp.Inventory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('discount', models.IntegerField(default=0)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('customer', models.ForeignKey(to='vkapp.Customer')),
                ('products', models.ManyToManyField(to='vkapp.Inventory', through='vkapp.ProductSales')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='productsales',
            name='sales',
            field=models.ForeignKey(to='vkapp.Sales'),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vkapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='total',
            field=models.DecimalField(default=0.0, max_digits=11, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inventory',
            name='selling_price',
            field=models.DecimalField(default=0.0, max_digits=11, decimal_places=2),
        ),
    ]

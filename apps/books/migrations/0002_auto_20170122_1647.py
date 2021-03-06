# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 16:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_remove_user_birthday'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set([('user', 'book')]),
        ),
    ]

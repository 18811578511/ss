# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-12 11:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerifyCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, verbose_name='\u9a8c\u8bc1\u7801')),
                ('mobile', models.CharField(max_length=11, verbose_name='\u7535\u8bdd')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u77ed\u4fe1\u9a8c\u8bc1\u7801',
                'verbose_name_plural': '\u77ed\u4fe1\u9a8c\u8bc1\u7801',
            },
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-08 21:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equip_type',
            fields=[
                ('type_id1', models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='\u8bbe\u5907\u5206\u7c7bID')),
                ('type_big1', models.CharField(max_length=100, verbose_name='\u8bbe\u5907\u5927\u7c7b\u522b')),
                ('type_small1', models.CharField(max_length=100, verbose_name='\u8bbe\u5907\u5c0f\u7c7b\u522b')),
            ],
            options={
                'verbose_name': '\u8bbe\u5907\u5206\u7c7b',
                'verbose_name_plural': '\u8bbe\u5907\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('equip_id', models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='\u8bbe\u5907ID')),
                ('equip_type', models.CharField(choices=[('Equipment', '\u8bbe\u5907'), ('Software', '\u8f6f\u4ef6'), ('Technology', '\u6280\u672f')], max_length=10)),
                ('equip_name', models.CharField(max_length=100, verbose_name='\u8bbe\u5907\u540d\u79f0')),
                ('produce_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u751f\u4ea7\u65e5\u671f')),
                ('equip_over', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u5230\u671f\u5e74\u9650')),
                ('equip_owner', models.IntegerField(default=0, verbose_name='\u8bbe\u5907\u6240\u5c5e')),
                ('equip_expense', models.FloatField(default=0.0, verbose_name='\u8bbe\u5907\u4ef7\u683c')),
                ('equip_start', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u51fa\u79df\u5f00\u59cb\u65f6\u95f4')),
                ('equip_end', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u51fa\u79df\u7ed3\u675f\u65f6\u95f4')),
                ('equip_price', models.FloatField(default=0.0, verbose_name='\u51fa\u79df\u8d39\u7528')),
                ('equip_picture', models.CharField(default='\u8bbe\u5907\u56fe\u7247', max_length=100)),
                ('equip_typeb', models.CharField(max_length=100, verbose_name='\u8bbe\u5907\u5927\u7c7b\u522b')),
                ('equip_types', models.CharField(max_length=100, verbose_name='\u8bbe\u5907\u5c0f\u7c7b\u522b')),
                ('equip_parameter', models.TextField(verbose_name='\u6027\u80fd\u53c2\u6570')),
                ('equip_place', models.TextField(verbose_name='\u5730\u70b9')),
                ('equip_comment', models.CharField(max_length=300, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u8bbe\u5907',
                'verbose_name_plural': '\u8bbe\u5907',
            },
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('software_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='\u8bbe\u5907ID')),
                ('software_type', models.CharField(choices=[('Equipment', '\u8bbe\u5907'), ('Software', '\u8f6f\u4ef6'), ('Technology', '\u6280\u672f')], max_length=10)),
                ('software_name', models.CharField(max_length=100, verbose_name='\u8f6f\u4ef6\u540d\u79f0')),
                ('software_owner', models.IntegerField(default=0, verbose_name='\u8f6f\u4ef6\u6240\u5c5e')),
                ('software_expense', models.FloatField(default=0.0, verbose_name='\u8f6f\u4ef6\u4ef7\u683c')),
                ('software_start', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u51fa\u79df\u5f00\u59cb\u65f6\u95f4')),
                ('software_end', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u51fa\u79df\u7ed3\u675f\u65f6\u95f4')),
                ('software_price', models.FloatField(default=0.0, verbose_name='\u51fa\u79df\u8d39\u7528')),
                ('software_image', models.CharField(default='\u8f6f\u4ef6\u56fe\u7247', max_length=100)),
                ('oftware_typeb', models.CharField(max_length=100, verbose_name='\u8f6f\u4ef6\u5927\u7c7b\u522b')),
                ('equip_types', models.CharField(max_length=100, verbose_name='\u8f6f\u4ef6\u5c0f\u7c7b\u522b')),
                ('software_describe', models.TextField(verbose_name='\u8f6f\u4ef6\u63cf\u8ff0')),
                ('os', models.CharField(max_length=100, verbose_name='\u8fd0\u884c\u5e73\u53f0')),
                ('software_comment', models.CharField(max_length=300, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u8f6f\u4ef6',
                'verbose_name_plural': '\u8f6f\u4ef6',
            },
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('tech_id', models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='\u6280\u672fID')),
                ('tech_type', models.CharField(choices=[('Equipment', '\u8bbe\u5907'), ('Software', '\u8f6f\u4ef6'), ('Technology', '\u6280\u672f')], max_length=10)),
                ('tech_name', models.CharField(max_length=100, verbose_name='\u6280\u672f\u540d\u79f0')),
                ('tech_info', models.CharField(max_length=300, verbose_name='\u6280\u672f\u670d\u52a1\u4fe1\u606f')),
                ('tech_typeb', models.CharField(max_length=100, verbose_name='\u6280\u672f\u5927\u7c7b\u522b')),
                ('tech_types', models.CharField(max_length=100, verbose_name='\u6280\u672f\u5c0f\u7c7b\u522b')),
                ('tech_owner', models.IntegerField(default=0, verbose_name='\u6280\u672f\u6240\u5c5e')),
                ('tech_price', models.FloatField(default=0.0, verbose_name='\u6280\u672f\u4ef7\u683c')),
                ('tech_image', models.CharField(default='\u6280\u672f\u56fe\u7247', max_length=100)),
                ('tech_commet', models.CharField(max_length=300, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u6280\u672f',
                'verbose_name_plural': '\u6280\u672f',
            },
        ),
    ]
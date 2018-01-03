# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-27 01:37
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shizhi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='试纸名称')),
                ('slug', models.CharField(max_length=20, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='试纸介绍')),
                ('shiyong', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='使用介绍')),
                ('is_taozhuang', models.BooleanField(default=False, verbose_name='是否是套装')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '试纸',
                'verbose_name_plural': '试纸',
            },
        ),
    ]

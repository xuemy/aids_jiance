# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-08 12:32
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extendsite',
            name='baidu_analytics',
        ),
        migrations.RemoveField(
            model_name='extendsite',
            name='google_analytics',
        ),
        migrations.AddField(
            model_name='extendsite',
            name='analytics',
            field=models.CharField(blank=True, max_length=40, verbose_name='统计代码'),
        ),
        migrations.AddField(
            model_name='extendsite',
            name='shiyong',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='试纸使用方法'),
        ),
        migrations.AddField(
            model_name='extendsite',
            name='zice',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='自测症状持续添加'),
        ),
        migrations.AlterField(
            model_name='friendlink',
            name='site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friendlink', to='sites.Site'),
        ),
    ]

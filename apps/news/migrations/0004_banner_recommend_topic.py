# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-15 18:25
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0003_article_cover_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='主键')),
                ('title', models.CharField(max_length=20, verbose_name='标题')),
                ('desc', models.CharField(max_length=100, verbose_name='描述')),
                ('image', models.ImageField(upload_to='article/banner/%Y/%m', verbose_name='封面')),
                ('href', models.URLField(blank=True, default=None, null=True, verbose_name='图片链接')),
                ('order', models.IntegerField(default=10, help_text='排序字段', verbose_name='排序')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间')),
                ('is_del', models.IntegerField(choices=[(0, '未删除'), (1, '已删除')], default=0, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '新闻轮播图',
                'verbose_name_plural': '新闻轮播图',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='主键')),
                ('title', models.CharField(max_length=20, unique=True, verbose_name='主题名')),
                ('cover_img', models.ImageField(default=None, upload_to='article/topic/%Y/%m', verbose_name='封面照片')),
                ('desc', models.CharField(max_length=100, verbose_name='主题描述')),
                ('hits', models.IntegerField(default=0, verbose_name='点击量')),
                ('is_recommend', models.IntegerField(choices=[(0, '未推荐'), (1, '已推荐')], default=0, verbose_name='是否推荐')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间')),
                ('is_del', models.IntegerField(choices=[(0, '未删除'), (1, '已删除')], default=0, verbose_name='是否删除')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建用户')),
            ],
            options={
                'verbose_name': '主题',
                'verbose_name_plural': '主题',
            },
        ),
        migrations.CreateModel(
            name='Recommend',
            fields=[
            ],
            options={
                'verbose_name': '编辑推荐',
                'verbose_name_plural': '编辑推荐',
                'proxy': True,
                'indexes': [],
            },
            bases=('news.topic',),
        ),
    ]

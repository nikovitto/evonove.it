# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 11:37
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='bio',
            field=wagtail.wagtailcore.fields.RichTextField(help_text='The team member bio', max_length=1000),
        ),
    ]

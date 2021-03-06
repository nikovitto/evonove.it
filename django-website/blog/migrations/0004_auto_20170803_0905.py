# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 09:05
from __future__ import unicode_literals

import blog.fields
from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170310_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('h2', wagtail.wagtailcore.blocks.CharBlock(icon='title')), ('h3', wagtail.wagtailcore.blocks.CharBlock(icon='title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('alignment', blog.fields.ImageFormatBlock()), ('caption', wagtail.wagtailcore.blocks.RichTextBlock(required=False))), icon='image', label='Aligned image')), ('youtube', wagtail.wagtailembeds.blocks.EmbedBlock(icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock(label='Quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())), icon='openquote')), ('code_snippet', wagtail.wagtailcore.blocks.StructBlock((('language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('python', 'Python'), ('cpp', 'C++'), ('html', 'HTML'), ('css', 'CSS')])), ('code_text', wagtail.wagtailcore.blocks.TextBlock())), icon='code', label='Code Snippet')))),
        ),
    ]

# Generated by Django 3.0.7 on 2020-06-30 08:36

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0004_testcase_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='input_specification',
            field=ckeditor.fields.RichTextField(default='Nothing'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problem',
            name='output_specification',
            field=ckeditor.fields.RichTextField(default='Nothing'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='problem',
            name='statement',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
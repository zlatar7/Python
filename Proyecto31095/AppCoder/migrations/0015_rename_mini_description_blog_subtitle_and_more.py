# Generated by Django 4.1 on 2022-10-02 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0014_blog_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='mini_description',
            new_name='subtitle',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='name',
            new_name='title',
        ),
    ]
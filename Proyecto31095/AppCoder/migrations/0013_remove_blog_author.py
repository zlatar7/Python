# Generated by Django 4.1 on 2022-10-02 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0012_rename_date_blog_post_date_remove_blog_subtitle_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
    ]
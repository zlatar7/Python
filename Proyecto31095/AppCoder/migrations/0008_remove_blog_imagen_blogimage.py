# Generated by Django 4.1 on 2022-10-01 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0007_blog_autor_blog_contenido_blog_imagen_blog_subtitulo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='imagen',
        ),
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='media')),
                ('nombre', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AppCoder.blog')),
            ],
        ),
    ]
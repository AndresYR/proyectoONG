# Generated by Django 4.1.4 on 2022-12-19 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_posteo_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteo',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
# Generated by Django 2.2.7 on 2019-12-02 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorymanager', '0002_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
# Generated by Django 2.2.7 on 2019-11-21 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uprofile', '0002_user_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.FileField(default='no-image-user', upload_to='avatars'),
        ),
    ]

# Generated by Django 2.2.7 on 2019-11-21 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uprofile', '0004_auto_20191121_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.FileField(default='no-image-user.png', upload_to='avatars/'),
        ),
    ]

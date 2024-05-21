# Generated by Django 5.0.4 on 2024-05-20 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_rename_user_id_userinfo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='company',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='image',
            field=models.ImageField(default=None, upload_to='image'),
        ),
    ]

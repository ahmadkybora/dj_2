# Generated by Django 4.1.1 on 2022-09-06 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_user_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default=1, max_length=200, verbose_name='نام'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default=1, max_length=200, verbose_name='نام خانوادگی'),
            preserve_default=False,
        ),
    ]

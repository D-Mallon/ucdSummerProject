# Generated by Django 4.2.2 on 2023-07-08 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userroute'),
    ]

    operations = [
        migrations.AddField(
            model_name='userroute',
            name='hour',
            field=models.IntegerField(default=12, verbose_name='Hour'),
            preserve_default=False,
        ),
    ]

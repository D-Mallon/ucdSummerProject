# Generated by Django 4.0.10 on 2023-07-18 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_nodes_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='nodes',
            name='id_str',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
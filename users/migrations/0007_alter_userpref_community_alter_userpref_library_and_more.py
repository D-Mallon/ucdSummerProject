# Generated by Django 4.0.10 on 2023-07-20 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_userpref_park'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpref',
            name='community',
            field=models.CharField(default=' ', max_length=300, verbose_name='Community Centres'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userpref',
            name='library',
            field=models.CharField(default=' ', max_length=300, verbose_name='Libraries'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userpref',
            name='museum',
            field=models.CharField(default=' ', max_length=300, verbose_name='Museums & Art Galleries'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userpref',
            name='park',
            field=models.CharField(max_length=300, verbose_name='Parks'),
        ),
        migrations.AlterField(
            model_name='userpref',
            name='park_node',
            field=models.CharField(default=' ', max_length=300, verbose_name='Other Park Nodes'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userpref',
            name='walking_node',
            field=models.CharField(default=' ', max_length=300, verbose_name='Other Walking Nodes'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userpref',
            name='worship',
            field=models.CharField(default=' ', max_length=300, verbose_name='Places of Worship'),
            preserve_default=False,
        ),
    ]

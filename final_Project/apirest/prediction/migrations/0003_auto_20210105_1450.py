# Generated by Django 3.1.4 on 2021-01-05 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0002_auto_20201210_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='YEAR',
        ),
        migrations.AddField(
            model_name='song',
            name='YEAR_MAX',
            field=models.FloatField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='song',
            name='YEAR_MIN',
            field=models.FloatField(null='True'),
            preserve_default='True',
        ),
    ]

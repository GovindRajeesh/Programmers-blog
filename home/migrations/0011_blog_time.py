# Generated by Django 3.0.9 on 2020-08-04 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20200804_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='Time',
            field=models.TimeField(default=''),
            preserve_default=False,
        ),
    ]

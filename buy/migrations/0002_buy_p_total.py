# Generated by Django 4.1.1 on 2022-09-26 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='p_total',
            field=models.IntegerField(default=5000),
            preserve_default=False,
        ),
    ]

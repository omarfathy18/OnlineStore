# Generated by Django 4.1.1 on 2022-09-27 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='p_img',
            field=models.CharField(default='img', max_length=200),
            preserve_default=False,
        ),
    ]

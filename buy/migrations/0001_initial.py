# Generated by Django 4.1.1 on 2022-09-24 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('p_name', models.CharField(max_length=50)),
                ('p_price', models.IntegerField()),
                ('p_state', models.BooleanField(default=0)),
                ('p_quantity', models.IntegerField()),
            ],
        ),
    ]
# Generated by Django 3.2 on 2021-05-29 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genel', '0005_sosyalmedya'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adres', models.TextField(verbose_name='West-Gate Adres')),
            ],
        ),
    ]
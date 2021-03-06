# Generated by Django 3.2 on 2021-05-30 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeri', '0006_auto_20210530_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galerivideo',
            name='alt_baslik',
            field=models.CharField(default=' ', max_length=256, verbose_name='Video Alt Yazı'),
        ),
        migrations.AlterField(
            model_name='galerivideo',
            name='baslik',
            field=models.CharField(default='West Gate', max_length=64, verbose_name='Video Başlığı'),
        ),
        migrations.AlterField(
            model_name='galerivideo',
            name='orta_baslik',
            field=models.CharField(default=' ', max_length=128, verbose_name='Video Orta Yazı'),
        ),
    ]

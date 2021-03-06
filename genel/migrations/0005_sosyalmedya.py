# Generated by Django 3.2 on 2021-05-29 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genel', '0004_remove_duyuru_duyuru_kenar_karartma_renkkodu'),
    ]

    operations = [
        migrations.CreateModel(
            name='SosyalMedya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, verbose_name='Twitter')),
                ('linkedin', models.URLField(blank=True, verbose_name='Linkedin')),
                ('google', models.URLField(blank=True, verbose_name='Google+')),
                ('rss', models.URLField(blank=True, verbose_name='Rss')),
                ('pinterest', models.URLField(blank=True, verbose_name='Pinterest')),
                ('whatsapp', models.URLField(blank=True, verbose_name='Whatsapp')),
            ],
            options={
                'verbose_name_plural': 'Sosyal Medya',
            },
        ),
    ]

# Generated by Django 3.2 on 2021-05-30 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeri', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='galeri',
            name='islem',
            field=models.CharField(default='Değiştirmek için dokunun', editable=False, max_length=32, verbose_name='Hızlı İşlem'),
        ),
    ]

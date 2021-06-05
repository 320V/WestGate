# Generated by Django 3.2 on 2021-05-30 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hakkimizda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AltKutucuk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kutu_basligi', models.CharField(max_length=16, verbose_name='Başlık')),
                ('kutu_icerigi', models.TextField(max_length=64, verbose_name='İçerik')),
                ('guncelleme_tarihi', models.DateField(default='2021-05-30', editable=False, verbose_name='Son Güncelleme')),
            ],
            options={
                'verbose_name_plural': 'Bilgilendirme Kutuları',
            },
        ),
        migrations.AlterField(
            model_name='ustbolum',
            name='ikinci_parag',
            field=models.TextField(blank=True, help_text='2. paragraf eklemek istiyorsanız burayı doldurun.', max_length=256, verbose_name='İkinci Paragraf'),
        ),
        migrations.AlterField(
            model_name='ustbolum',
            name='ilk_parag',
            field=models.TextField(max_length=1024, verbose_name='Hakkımızda'),
        ),
    ]
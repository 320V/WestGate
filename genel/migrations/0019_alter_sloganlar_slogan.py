# Generated by Django 3.2 on 2021-05-29 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genel', '0018_auto_20210529_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sloganlar',
            name='slogan',
            field=models.CharField(help_text='Bu alan üst sol bölümde, bilgilendirme veya uyarı amacıyla kullanılabilir mesajlar bırakmanızı sağlar.', max_length=256, verbose_name='Mesajınız'),
        ),
    ]

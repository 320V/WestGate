# Generated by Django 3.2 on 2021-05-29 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genel', '0016_rename_tik_logo_islem'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyukResimBilgilendirme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(blank=True, max_length=32, verbose_name='Başlık')),
                ('aciklama', models.TextField(blank=True, max_length=64, verbose_name='Açıklama')),
                ('resim', models.ImageField(help_text='Resim boyutunun netlik için büyük olduğundan emin olun.', upload_to='', verbose_name='Arkaplan Resmi')),
                ('buton_txt', models.CharField(help_text='Buton görünmesini istemiyorsanız boş bırakabilirsiniz.', max_length=24, verbose_name='Buton Yazısı')),
                ('buton_url', models.URLField(help_text='Butona tıklanıldığında gidilmesini istediğiniz adresi giriniz.', verbose_name='Buton Yönlendirdiği Link')),
            ],
            options={
                'verbose_name_plural': 'Giriş Ekranı',
            },
        ),
        migrations.AlterField(
            model_name='logo',
            name='islem',
            field=models.CharField(default='Değiştirmek için dokunun', editable=False, max_length=32, verbose_name='Hızlı İşlem'),
        ),
    ]

from django.db import models
from datetime import datetime
class UstBolum(models.Model):
    baslik = models.CharField(verbose_name='Başlık',max_length=32)
    ilk_parag = models.TextField(verbose_name='Hakkımızda',max_length=1024)
    ikinci_parag = models.TextField(verbose_name='İkinci Paragraf',max_length=1024,help_text='2. paragraf eklemek istiyorsanız burayı doldurun.',blank=True)
    guncelleme_tarihi = models.DateField(verbose_name='Son Güncelleme',default=datetime.now().strftime('%Y-%m-%d'), editable=False)
    def __str__(self):
        return 'Üst Bölüm'
    class Meta:
        verbose_name_plural = 'Üst Bölüm'
class YanBuyukResim(models.Model):
    rsm = models.ImageField(verbose_name='Yan Resim')
    guncelleme_tarihi = models.DateField(verbose_name='Son Güncelleme',default=datetime.now().strftime('%Y-%m-%d'), editable=False)
    def __str__(self):
        return 'Yan Büyük Resim'
    class Meta:
        verbose_name_plural = 'Yan Büyük Resim'
class AltKutucuk(models.Model):
    kutu_basligi = models.CharField(verbose_name='Başlık',max_length=32)
    kutu_icerigi = models.TextField(verbose_name='İçerik',max_length=256)
    guncelleme_tarihi = models.DateField(verbose_name='Son Güncelleme',default=datetime.now().strftime('%Y-%m-%d'), editable=False)
    def __str__(self):
        return 'Bilgilendirme Kutuları'
    class Meta:
        verbose_name_plural = 'Bilgilendirme Kutuları'


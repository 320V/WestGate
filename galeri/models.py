from django.db import models
from datetime import datetime
from .validators import validate_file_extension

class Galeri(models.Model):
    rsm = models.ImageField(verbose_name='Resim')
    baslik = models.CharField(verbose_name='Resim Başlığı',max_length=64)
    aciklama = models.TextField(verbose_name='Açıklama',max_length=128)
    guncelleme_tarihi = models.DateField(verbose_name='Yayınlanma Tarihi',default=datetime.now().strftime('%Y-%m-%d'), editable=False)
    islem = models.CharField(verbose_name='Hızlı İşlem', default='Değiştirmek için dokunun', editable=False,max_length=32)
    def __str__(self):
        return 'Resim'
    class Meta:
        verbose_name_plural = 'Resim'

class GaleriVideo(models.Model):
    video = models.FileField(verbose_name='Video', validators=[validate_file_extension], default='.mp4')
    baslik = models.CharField(verbose_name='Video Başlığı',max_length=64,default='West Gate',blank=True)
    orta_baslik = models.CharField(verbose_name='Video Orta Yazı',max_length=128,default=' ',blank=True)
    alt_baslik = models.CharField(verbose_name='Video Alt Yazı',max_length=256,default=' ',blank=True)
    kaydirma_rsm = models.ImageField(verbose_name='Kaydırma Resmi',default='')
    guncelleme_tarihi = models.DateField(verbose_name='Yayınlanma Tarihi', default=datetime.now().strftime('%Y-%m-%d'),editable=False)
    islem = models.CharField(verbose_name='Hızlı İşlem', default='Düzenle', editable=False,max_length=32)
    def __str__(self):
        return 'Video'
    class Meta:
        verbose_name_plural = 'Video'

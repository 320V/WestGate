from django.db import models
from datetime import datetime

class Duyuru(models.Model):
    duyuru_basligi = models.CharField(verbose_name='Duyuru Başlığı',max_length=32)
    duyuru_metni = models.TextField(verbose_name='Duyuru Metni', max_length=256)
    guncelleme_tarihi = models.DateField(verbose_name='Yayınlanma Tarihi',default=datetime.now().strftime('%Y-%m-%d'), editable=False)
    def __str__(self):
        return 'Duyuru'
    class Meta:
        verbose_name_plural = 'Duyuru'

from django.db import models
from datetime import datetime

class Duyuru(models.Model):
    duyuru_baslik = models.CharField(max_length=32,verbose_name='Duyuru Başlığı')
    duyuru_text = models.TextField(verbose_name='Duyuru Metni')
    duyuru_arkaplan_resmi = models.URLField(verbose_name='Duyuru Arkaplan Resmi',default='https://www.akisaluminyum.com.tr/assets/filter/img/407604122west_gate_banner.jpg',help_text="Arkaplanda gözükmesini istediğiniz resme ait URL'yi girin.")
    duyuru_yayinlanma_tarihi = models.DateField(default=datetime.now().strftime('%Y-%m-%d'),editable=False)
    def __str__(self):
        return 'Ana Sayfa Duyuru'

    class Meta:
        verbose_name_plural = 'Ana Sayfa Duyuru'

class SosyalMedya(models.Model):
    facebook = models.URLField(verbose_name='Facebook',blank=True,help_text='Yönlendirilmesini istediğiniz facebook profil adresini girin.')
    twitter = models.URLField(verbose_name='Twitter',blank=True,help_text='Yönlendirilmesini istediğiniz twitter profil adresini girin.')
    linkedin = models.URLField(verbose_name='Linkedin',blank=True,help_text='Yönlendirilmesini istediğiniz linkedin profil adresini girin.')
    google = models.CharField(verbose_name='Google+',blank=True,max_length=128,help_text='Yönlendirilmesini istediğiniz mail adresini girin.')
    rss = models.URLField(verbose_name='Rss',blank=True,help_text='Yönlendirilmesini istediğiniz rss adresini girin.')
    pinterest= models.URLField(verbose_name='Pinterest',blank=True,help_text='Yönlendirilmesini istediğiniz pinterest adresini girin.')
    whatsapp = models.CharField(verbose_name='Whatsapp',blank=True,help_text='Yönlendirilmesini istediğiniz telefon numarasını giriniz.',max_length=32)
    def __str__(self):
        return 'Sosyal Medya'
    class Meta:
        verbose_name_plural = 'Sosyal Medya'

class Adres(models.Model):
    adres = models.TextField(verbose_name='West-Gate Adres',default='Konutkent, Dumlupınar Blv. No:391, 06810 Çankaya/Ankara')
    def __str__(self):
        return 'Adres'
    class Meta:
        verbose_name_plural = 'Adres'

class Telefonlar(models.Model):
    yonetim_tel = models.CharField(verbose_name='Yönetim Telefon',max_length=32)
    muhasebe_tel = models.CharField(verbose_name='Muhasebe Telefon',max_length=32)
    halklailiskiler_tel = models.CharField(verbose_name='Halkla İlişkiler Telefon',max_length=32)
    a_resep_tel = models.CharField(verbose_name='A Resepsiyon Telefon',max_length=32,blank=True,help_text='Bu alan boş bırakılabilir.')
    b_resep_tel = models.CharField(verbose_name='B Resepsiyon Telefon',max_length=32,blank=True,help_text='Bu alan boş bırakılabilir.')
    c_resep_tel = models.CharField(verbose_name='C Resepsiyon Telefon',max_length=32,blank=True,help_text='Bu alan boş bırakılabilir.')
    guncelleme_tarihi = models.DateField(verbose_name='Son Güncelleme', default=datetime.now().strftime('%Y-%m-%d'),
                                         editable=False)
    def __str__(self):
        return 'Telefon Bilgileri'
    class Meta:
        verbose_name_plural = 'Telefon Bilgileri'

class Mailler(models.Model):
    yonetim_mail = models.CharField(verbose_name='Yönetim E-Mail',max_length=32)
    muhasebe_mail = models.CharField(verbose_name='Muhasebe E-Mail',max_length=32)
    halklailiskiler_mail = models.CharField(verbose_name='Halkla İlişkiler E-Mail',max_length=32)
    guncelleme_tarihi = models.DateField(verbose_name='Son Güncelleme',default=datetime.now().strftime('%Y-%m-%d'), editable=False)
    def __str__(self):
        return 'E-Mail Bilgileri'
    class Meta:
        verbose_name_plural = 'E-Mail Bilgileri'

class AnaHakkimizda(models.Model):
    ana_hakkimizda = models.TextField(verbose_name='Hakkımızda',help_text="Bu bölüm 'Ana Sayfa'nızın sol alt köşesinde görünür.",max_length=256)
    guncelleme_tarihi = models.DateField(verbose_name='Son Güncelleme',default=datetime.now().strftime('%Y-%m-%d'), editable=False)
    def __str__(self):
        return 'Hakkımızda'
    class Meta:
        verbose_name_plural = 'Hakkımızda'

class Sloganlar(models.Model):
    slogan = models.CharField(verbose_name='Mesajınız',help_text='Bu alan üst sol bölümde, bilgilendirme veya uyarı amacıyla kullanılabilir mesajlar bırakmanızı sağlar.',max_length=64)
    guncelleme_tarihi = models.DateField(verbose_name='Son Güncelleme',default=datetime.now().strftime('%Y-%m-%d'), editable=False)
    def __str__(self):
        return 'Üst Mesajlar'
    class Meta:
        verbose_name_plural = 'Üst Mesajlar'

class Logo(models.Model):
    logo = models.ImageField(verbose_name='Logo',help_text='Önerilen Boyutlar: 150x50 (Daha büyük boyutlar sayfa üst bölgesinde kaymalara sebep olabilir.)')
    islem = models.CharField(verbose_name='Hızlı İşlem',default='Değiştirmek için dokunun',editable=False,max_length=32)
    def __str__(self):
        return 'Logo'
    class Meta:
        verbose_name_plural = 'Logo'

class BuyukResimBilgilendirme(models.Model):
    baslik = models.CharField(verbose_name='Başlık',blank=True,max_length=32)
    aciklama = models.TextField(verbose_name='Açıklama',blank=True,max_length=64)
    resim = models.ImageField(verbose_name='Arkaplan Resmi',help_text='Resim boyutunun netlik için büyük olduğundan emin olun.')
    buton_txt = models.CharField(verbose_name='Buton Yazısı',blank=True,help_text='Buton görünmesini istemiyorsanız boş bırakabilirsiniz.',max_length=24)
    buton_url = models.URLField(verbose_name='Buton Yönlendirdiği Link',blank=True,help_text='Butona tıklanıldığında gidilmesini istediğiniz adresi giriniz.')
    islem = models.CharField(verbose_name='Hızlı İşlem', default='Değiştirmek için dokunun', editable=False,max_length=32)
    def __str__(self):
        return 'Giriş Ekranı'
    class Meta:
        verbose_name_plural = 'Giriş Ekranı'

class InstagramGaleri(models.Model):
    resim = models.ImageField(verbose_name='Resim')
    resim_url = models.URLField(verbose_name='Resim Instagram Linki')
    eklenme_tarihi = models.DateField(verbose_name='Eklenme Tarihi', default=datetime.now().strftime('%Y-%m-%d'),editable=False)
    islem = models.CharField(verbose_name='Hızlı İşlem', default='Düzenle', editable=False,max_length=32)
    def __str__(self):
        return 'Instagram Galerisi'
    class Meta:
        verbose_name_plural = 'Instagram Galerisi'

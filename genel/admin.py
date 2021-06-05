from django.contrib import admin
from genel.models import Duyuru,SosyalMedya,Adres,Telefonlar,Mailler,AnaHakkimizda,Sloganlar,Logo,BuyukResimBilgilendirme,InstagramGaleri

class DuyuruAdmin(admin.ModelAdmin):
    list_display = ['duyuru_baslik', 'duyuru_text','duyuru_yayinlanma_tarihi']
    list_display_links = ['duyuru_baslik', 'duyuru_text']
    def has_add_permission(self, request):
        izin_verilen_eleman_sayisi = 1
        if self.model.objects.count() >= izin_verilen_eleman_sayisi:
            return False
        return super().has_add_permission(request)
    class Meta:
        model= Duyuru

class SosyalMedyaAdmin(admin.ModelAdmin):
    list_display = ['facebook','linkedin','linkedin','google','rss','pinterest','whatsapp']
    list_display_links = ['facebook','linkedin','linkedin','google','rss','pinterest','whatsapp']
    def has_add_permission(self, request):
        izin_verilen_eleman_sayisi = 1
        if self.model.objects.count() >= izin_verilen_eleman_sayisi:
            return False
        return super().has_add_permission(request)
    class Meta:
        model=SosyalMedya

class AdresAdmin(admin.ModelAdmin):
    list_display = ['adres']
    list_display_links = ['adres']
    def has_add_permission(self, request):
        izin_verilen_eleman_sayisi = 1
        if self.model.objects.count() >= izin_verilen_eleman_sayisi:
            return False
        return super().has_add_permission(request)
    class Meta:
        model=SosyalMedya

class TelefonlarAdmin(admin.ModelAdmin):
    list_display = ['yonetim_tel','muhasebe_tel','halklailiskiler_tel','a_resep_tel','b_resep_tel','c_resep_tel','guncelleme_tarihi']
    list_display_links = ['yonetim_tel','muhasebe_tel','halklailiskiler_tel','a_resep_tel','b_resep_tel','c_resep_tel']
    def has_add_permission(self, request):
        izin_verilen_eleman_sayisi = 1
        if self.model.objects.count() >= izin_verilen_eleman_sayisi:
            return False
        return super().has_add_permission(request)
    class Meta:
        model=Telefonlar

class MaillerAdmin(admin.ModelAdmin):
    list_display = ['yonetim_mail','muhasebe_mail','halklailiskiler_mail','guncelleme_tarihi']
    list_display_links = ['yonetim_mail','muhasebe_mail','halklailiskiler_mail']
    def has_add_permission(self, request):
        izin_verilen_eleman_sayisi = 1
        if self.model.objects.count() >= izin_verilen_eleman_sayisi:
            return False
        return super().has_add_permission(request)
    class Meta:
        model=Mailler

class AnaHakkimizdaAdmin(admin.ModelAdmin):
    list_display = ['ana_hakkimizda','guncelleme_tarihi']
    list_display_links = ['ana_hakkimizda']
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)
    class Meta:
        pass
    model=AnaHakkimizda

class SloganlarAdmin(admin.ModelAdmin):
    list_display = ['slogan','guncelleme_tarihi']
    list_display = ['slogan']
    class Meta:
        pass
    model=Sloganlar

class LogoAdmin(admin.ModelAdmin):
    list_display = ['logo','islem']
    list_display_links = ['logo','islem']
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)
    class Meta:
        pass
    model = Logo

class BuyukResimBilgilendirmeAdmin(admin.ModelAdmin):
    list_display = ['baslik','aciklama','resim','buton_txt','buton_url','islem']
    list_display_links = ['baslik','aciklama','resim','buton_txt','buton_url','islem']
    class Meta:
        pass
    model = BuyukResimBilgilendirme

class InstagramGaleriAdmin(admin.ModelAdmin):
    list_display = ['resim','resim_url','eklenme_tarihi','islem']
    list_display_links = ['resim','resim_url','islem']
    class Meta:
        pass
    model = InstagramGaleri

admin.site.register(Duyuru,DuyuruAdmin)
admin.site.register(SosyalMedya,SosyalMedyaAdmin)
admin.site.register(Adres,AdresAdmin)
admin.site.register(Telefonlar,TelefonlarAdmin)
admin.site.register(Mailler,MaillerAdmin)
admin.site.register(AnaHakkimizda,AnaHakkimizdaAdmin)
admin.site.register(Sloganlar,SloganlarAdmin)
admin.site.register(Logo,LogoAdmin)
admin.site.register(BuyukResimBilgilendirme,BuyukResimBilgilendirmeAdmin)
admin.site.register(InstagramGaleri,InstagramGaleriAdmin)


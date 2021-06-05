from django.contrib import admin
from hakkimizda.models import UstBolum,AltKutucuk,YanBuyukResim

class UstBolumAdmin(admin.ModelAdmin):
    list_display = ['baslik','ilk_parag','ikinci_parag','guncelleme_tarihi']
    list_display_links = ['baslik','ilk_parag','ikinci_parag']
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)
    class Meta:
        pass
    model = UstBolum
class YanBuyukResimAdmin(admin.ModelAdmin):
    list_display = ['rsm','guncelleme_tarihi']
    list_display_links = ['rsm']
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)
    class Meta:
        pass
    model = YanBuyukResim

class AltKutucukAdmin(admin.ModelAdmin):
    list_display = ['kutu_basligi','kutu_icerigi','guncelleme_tarihi']
    list_display_links = ['kutu_basligi','kutu_icerigi']
    class Meta:
        pass
    model = AltKutucuk


admin.site.register(UstBolum,UstBolumAdmin)
admin.site.register(AltKutucuk,AltKutucukAdmin)
admin.site.register(YanBuyukResim,YanBuyukResimAdmin)
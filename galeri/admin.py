from django.contrib import admin
from galeri.models import Galeri,GaleriVideo

class GaleriAdmin(admin.ModelAdmin):
    list_display = ['rsm','guncelleme_tarihi','islem']
    list_display_links = ['rsm','islem']
    class Meta:
        pass
    model = Galeri

class GaleriVideoAdmin(admin.ModelAdmin):
    list_display = ['video','baslik','orta_baslik','alt_baslik','kaydirma_rsm','guncelleme_tarihi','islem']
    list_display_links = ['video','baslik','orta_baslik','alt_baslik','islem']
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)
    class Meta:
        pass
    model = GaleriVideo

admin.site.register(Galeri,GaleriAdmin)
admin.site.register(GaleriVideo,GaleriVideoAdmin)

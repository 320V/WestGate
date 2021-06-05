from django.contrib import admin
from duyurular.models import Duyuru

class DuyuruAdmin(admin.ModelAdmin):
    list_display = ['duyuru_basligi','duyuru_metni','guncelleme_tarihi']
    list_display_links = ['duyuru_basligi','duyuru_metni']
    class Meta:
        pass
    model = Duyuru

admin.site.register(Duyuru,DuyuruAdmin)

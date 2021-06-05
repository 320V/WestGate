from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from genel.views import index
from iletisim.views import iletisim_index
from hakkimizda.views import hakkimizda_index
from duyurular.views import duyurular_index
from galeri.views import galeri_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('iletisim/',iletisim_index,name='iletisim'),
    path('hakkimizda/',hakkimizda_index,name='hakkimizda'),
    path('duyurular/',duyurular_index,name='duyurular'),
    path('galeri/',galeri_index,name='galeri'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

admin.site.site_header = "West-Gate Resisdence Web Admin Paneli"
admin.site.site_title = "West-Gate Resisdence Web Admin Giriş"
admin.site.index_title = "West-Gate Resisdence Web Admin Panel Yönetimi"
from django.shortcuts import render
from genel.models import Sloganlar, Logo, InstagramGaleri, SosyalMedya, Adres, Telefonlar, Mailler, InstagramGaleri
from galeri.models import Galeri,GaleriVideo

def galeri_index(request):
    context = dict()
    context['sosyal_medya'] = SosyalMedya.objects.all()
    context['adres_bilgisi'] = Adres.objects.all()
    context['telefon_bilgileri'] = Telefonlar.objects.all()
    context['mail_bilgileri'] = Mailler.objects.all()
    context['ust_reklam_bilgileri'] = Sloganlar.objects.all()
    context['logo_bilgisi'] = Logo.objects.all()
    context['instagram_galerisi'] = InstagramGaleri.objects.all()
    context['galeri_resimleri'] = Galeri.objects.all()
    context['galeri_video'] = GaleriVideo.objects.all()
    return render(request, 'galeri.html', context)

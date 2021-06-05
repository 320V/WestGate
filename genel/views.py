from django.shortcuts import render
from genel.models import Duyuru,SosyalMedya,Adres,Telefonlar,Mailler,AnaHakkimizda,Sloganlar,Logo,BuyukResimBilgilendirme,InstagramGaleri
from PIL import Image


def index(request):
    context = dict()
    context['duyuru_bilgileri'] = Duyuru.objects.all()
    context['sosyal_medya'] = SosyalMedya.objects.all()
    context['adres_bilgisi'] = Adres.objects.all()
    context['telefon_bilgileri'] = Telefonlar.objects.all()
    context['mail_bilgileri'] = Mailler.objects.all()
    context['anahakkimizda'] = AnaHakkimizda.objects.all()
    context['ust_reklam_bilgileri'] = Sloganlar.objects.all()
    context['logo_bilgisi'] = Logo.objects.all()
    context['buyuk_resim_bilgileri'] = BuyukResimBilgilendirme.objects.all()
    context['instagram_galerisi'] = InstagramGaleri.objects.all()

    return render(request,'index.html',context)

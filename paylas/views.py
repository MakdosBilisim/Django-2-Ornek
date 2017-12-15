from django.shortcuts import render

from paylas.models import Paylas


def anasayfa(request):
    print("anasayfa --> " + request.saatkac)
    kod_listesi = Paylas.objects.order_by('kayittarihi')
    return render(request, 'index.html', {'kod_listesi': kod_listesi})


def detay(request, slug):
    print("detay --> " + request.saatkac)

    try:

        kod_detayi = Paylas.objects.get(slug=slug)
        return render(request, 'detay.html', {'kod_detayi': kod_detayi})

    except Paylas.DoesNotExist:
        response = render(request, '404.html')
        response.status_code = 404
        return response

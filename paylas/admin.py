import json

import requests
from django.contrib import admin

from djiki.settings import GoogleShortUrlApi
from paylas.models import Paylas


def google_url_kisalt(url):
    req_url = 'https://www.googleapis.com/urlshortener/v1/url?key=' + GoogleShortUrlApi
    payload = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(req_url, json=payload, headers=headers)
    return json.loads(r.text)['id']


class PaylasAdmin(admin.ModelAdmin):
    list_display = ('baslik',)
    prepopulated_fields = {"slug": ("baslik",)}
    ordering = ('-kayittarihi',)
    readonly_fields = ('kisaurl',)
    list_per_page = 100
    date_hierarchy = 'kayittarihi'

    def save_model(self, request, obj, form, change):
        url_kisalt = google_url_kisalt("http:127.0.0.1:8000/" + obj.slug)
        obj.kisaurl = url_kisalt
        obj.save()


admin.site.register(Paylas, PaylasAdmin)

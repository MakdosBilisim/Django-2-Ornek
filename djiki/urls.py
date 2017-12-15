from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from paylas.views import anasayfa, detay

urlpatterns = [
                  path('admin/', admin.site.urls),

                  path('', anasayfa),
                  path('<slug:slug>/', detay),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

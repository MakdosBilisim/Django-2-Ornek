from django.db import models
from django.utils.translation import ugettext_lazy as _


class Paylas(models.Model):
    baslik = models.CharField(_('Başlık'), max_length=120, unique=True, help_text=_(u"En fazla 120 karakter olmalı."))
    icerik = models.TextField(_(u'İçerik'))
    slug = models.CharField(_('Otomatik Link'), max_length=71, help_text=_(u"En fazla 71 karakter olmalı."))
    kisaurl = models.CharField(_('Kısa URL'), max_length=20, default="")
    kayittarihi = models.DateTimeField(_(u'Kayıt Tarihi'), auto_now=True)

    def __str__(self):
        return '%s' % (self.baslik)

    class Meta:
        verbose_name_plural = _(u'Paylaşımlar')
        verbose_name = _(u'Kod')

# -*- coding: utf-8 -*-



try:
    from django.db import models
    from libs import current_site_url
    from django.core import urlresolvers
    from django.contrib.contenttypes.models import ContentType
except ImportError:
    from qtdjango import models

__author__ = 'darvin'


class UrlMixin(object):

    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return current_site_url() + urlresolvers.reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))
    get_admin_url.method_as_field = models.URLField(u"Ссылка")
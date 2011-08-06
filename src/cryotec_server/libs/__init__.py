# -*- coding: utf-8 -*-


def django_root_url(fq=False):
    """Returns base URL (no trailing slash) for the current project.

    Setting fq parameter to a true value will prepend the base URL
    of the current site to create a fully qualified URL.

    The name django_root_url is used in favor of alternatives
    (such as project_url) because it corresponds to the mod_python
    PythonOption django.root setting used in Apache.
    """
    from django.conf import settings

    url = getattr(settings, 'MY_DJANGO_URL_PATH', '')
    if fq:
        url = current_site_url() + url
    return url

def current_site_url():
    """Returns fully qualified URL (no trailing slash) for the current site."""
    from django.contrib.sites.models import Site
    from django.conf import settings

    current_site = Site.objects.get_current()
    protocol = getattr(settings, 'MY_SITE_PROTOCOL', 'http')
    port     = getattr(settings, 'MY_SITE_PORT', '')
    url = '%s://%s' % (protocol, current_site.domain)
    if port:
        url += ':%s' % port
    return url


def humanize_value(value):
    if value == 'None':
        return u"пусто"
    elif value=='False':
        return u"нет"
    elif value=='True':
        return u"да"
    else:
        return value
# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse, NoReverseMatch
from django.utils.translation import ugettext_lazy as _
from admin_tools.menu.items import AppList, MenuItem
from admin_tools.menu import Menu
from django.template.defaultfilters import capfirst
from django.conf import settings


class MyMenuAppList(AppList):
    def init_with_context(self, context):
        """
        Please refer to the :meth:`~admin_tools.menu.items.MenuItem.init_with_context`
        documentation from :class:`~admin_tools.menu.items.MenuItem` class.
        """
        settings_app_names = getattr(settings, "APP_NAMES", {})

        items = self._visible_models(context['request'])
        apps = {}
        for model, perms in items:
            if not perms['change']:
                continue
            app_label = model._meta.app_label
            if app_label not in apps:
                #FIXME: only this lines different!
                try:
                    title = settings_app_names[app_label]
                except KeyError:
                    title =  capfirst(app_label.title())
                apps[app_label] = {
                    'title': title,
                    'url': reverse('admin:app_list', args=(app_label,)),
                    'models': []
                }
            apps[app_label]['models'].append({
                'title': capfirst(model._meta.verbose_name_plural),
                'url': self._get_admin_change_url(model)
            })

        apps_sorted = apps.keys()
        apps_sorted.sort()
        for app in apps_sorted:
            app_dict = apps[app]
            item = MenuItem(title=app_dict['title'], url=app_dict['url'])
            # sort model list alphabetically
            apps[app]['models'].sort(lambda x, y: cmp(x['title'], y['title']))
            for model_dict in apps[app]['models']:
                item.children.append(MenuItem(**model_dict))
            self.children.append(item)



# to activate your custom menu add the following to your settings.py:
#
# ADMIN_TOOLS_MENU = 'cryotec_server.menu.CustomMenu'

class CustomMenu(Menu):
    """
    Custom Menu for cryotec_service admin site.
    """
    def __init__(self, **kwargs):
        Menu.__init__(self, **kwargs)
        try:
            self.children.append(MenuItem(
                title=_('Dashboard'),
                url=reverse('admin:index')
            ))
            self.children.append(MyMenuAppList(
                title=u"Управление данными",
                exclude_list=('django.contrib',"piston")
            ))
            self.children.append(MyMenuAppList(
                title=_('Administration'),
                include_list=('django.contrib',)
            ))
        except NoReverseMatch:
            pass

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        pass

# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard
from django.template.defaultfilters import capfirst
from django.conf import settings


class MyDashboardAppList(modules.AppList):
    def init_with_context(self, context):
        settings_app_names = getattr(settings, "APP_NAMES", {})

        items = self._visible_models(context['request'])
        apps = {}
        for model, perms in items:
            app_label = model._meta.app_label
            if app_label not in apps:
                #FIXME: only this lines different!
                try:
                    title = settings_app_names[app_label]
                except KeyError:
                    title =  capfirst(app_label.title())
                apps[app_label] = {
                    #FIXME: only this line different!
                    'title': title,
                    'url': reverse('admin:app_list', args=(app_label,)),
                    'models': []
                }
            model_dict = {}
            model_dict['title'] = capfirst(model._meta.verbose_name_plural)
            if perms['change']:
                model_dict['change_url'] = self._get_admin_change_url(model)
            if perms['add']:
                model_dict['add_url'] = self._get_admin_add_url(model)
            apps[app_label]['models'].append(model_dict)

        apps_sorted = apps.keys()
        apps_sorted.sort()
        for app in apps_sorted:
            # sort model list alphabetically
            apps[app]['models'].sort(lambda x, y: cmp(x['title'], y['title']))
            self.children.append(apps[app])

# to activate your index dashboard add the following to your settings.py:
#
# ADMIN_TOOLS_INDEX_DASHBOARD = 'cryotec_server.dashboard.CustomIndexDashboard'

class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for cryotec_server.
    """
    def __init__(self, **kwargs):
        Dashboard.__init__(self, **kwargs)

        # append a link list module for "quick links"
        self.children.append(modules.LinkList(
            title=_('Quick links'),
            layout='inline',
            draggable=False,
            deletable=False,
            collapsible=False,
            children=[
                {
                    'title': _('Change password'),
                    'url': reverse('admin:password_change'),
                },
                {
                    'title': _('Log out'),
                    'url': reverse('admin:logout')
                },
            ]
        ))

        # append an app list module for "Applications"
        self.children.append(MyDashboardAppList(
            title=u"Управление данными",
            exclude_list=('django.contrib',"piston",),
        ))

        # append an app list module for "Administration"
        self.children.append(modules.ModelList(
            title=_('Administration'),
            models=('django.contrib.*',),
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
            title=_('Recent Actions'),
            limit=10
        ))




    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        pass




# to activate your app index dashboard add the following to your settings.py:
#
# ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'cryotec_server.dashboard.CustomAppIndexDashboard'

class CustomAppIndexDashboard(AppIndexDashboard):
    """
    Custom app index dashboard for cryotec_server.
    """
    def __init__(self, *args, **kwargs):
        AppIndexDashboard.__init__(self, *args, **kwargs)

        # we disable title because its redundant with the model list module
        self.title = ''

        settings_app_names = getattr(settings, "APP_NAMES", {})
        try:
            title = settings_app_names[self.app_title.lower()]
        except KeyError:
            title =  self.app_title
        # append a model list module
        self.children.append(modules.ModelList(
            title=title,
            include_list=self.models,
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
            title=_('Recent Actions'),
            include_list=self.get_app_content_types(),
        ))

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        pass
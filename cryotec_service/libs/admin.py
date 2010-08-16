'''
@author: darvin
'''
from django.contrib import admin

#override of the InlineModelAdmin to support the link in the tabular inline
class LinkedInline(admin.options.InlineModelAdmin):
    template = "linked.html"
    admin_model_path = None
    extra = 0
    def __init__(self, *args):
        super(LinkedInline, self).__init__(*args)
        if self.admin_model_path is None:
            self.admin_model_path = self.model.__module__.split('.')[0] + "/" + self.model.__name__.lower()
            



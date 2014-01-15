from django.contrib import admin
from .models import Page, Template, Widget


'''
I would like to move to front-end editing of Page, Widgets as well as
Templates in the future. However, for now, I am enabling the respective
admins to get up and running with the proof-of-concept.
'''


class PageAdmin(admin.ModelAdmin):
    '''
    Defines django admin for the Page.
    '''
    exclude = ('slug',)
    list_display = ('slug', 'title', 'in_navbar', 'parent',)
    list_filter = ('in_navbar', 'parent',)

admin.site.register(Page, PageAdmin)


class TemplateAdmin(admin.ModelAdmin):
    '''
    Defines django admin for the Template.
    '''
    exclude = ('slug',)
    list_display = ('slug', 'title',)

admin.site.register(Template, TemplateAdmin)


class WidgetAdmin(admin.ModelAdmin):
    '''
    Defines django admin for the Widget.
    '''
    exclude = ('slug',)
    list_display = ('slug', 'title',)
    list_filter = ('page',)

admin.site.register(Widget, WidgetAdmin)

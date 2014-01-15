from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Page


def page(request, slug):
    '''
    The page view - produces a CMS2 page given the slug.
    '''
    nodes = Page.objects.filter(in_navbar=True)
    page = Page.objects.get(slug=slug)
    widgets = page.widgets.all()
    return render_to_response('forest/forest.html',
                              locals(),
                              context_instance=RequestContext(request))

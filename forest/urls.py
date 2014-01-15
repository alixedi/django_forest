from django.conf.urls import patterns, include, url


'''
These are our slugs - The CMS app has pages. Each page has
a unique slug allowing us to have a single view for furnishing
every page in CMS2.
'''

urlpatterns = patterns('forest.views',
   url(r'^(?P<slug>[\w-]+)/$', 'page', name='page'),
)

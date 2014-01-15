=============================
django_forest
=============================

.. image:: https://badge.fury.io/py/django_forest.png
    :target: http://badge.fury.io/py/django_forest
    
.. image:: https://travis-ci.org/alixedi/django_forest.png?branch=master
        :target: https://travis-ci.org/alixedi/django_forest

.. image:: https://pypip.in/d/django_forest/badge.png
        :target: https://crate.io/packages/django_forest?version=latest


Composite pages for django.

Installation
------------

We are at the cheese-shop: ::

    pip install django_forest

Usage
-----

In order to use django_forest in your project: ::

1. Include `mptt` and `forest` in your `INSTALLED_APPS` settings.
2. Enable `django-admin`.
3. In your terminal, type: `python manage.py syncdb`
4. Followed by: `python manage.py runserver`
5. Point your browser to `localhost:8000/admin`
6. Create a few `Pages`: Pages are defined as well, web-pages only that in context of django_forest, they contain `Widgets`.
7. Create a few `Widgets`: Little boxes that point to a URL. The URL is used to get a partial-HTML rendered from a server or JSON which is then rendered into HTML client-side using `handlebar.js` templates.
8. And finally we have `Templates`: If you haven't guessed already, these are client-side `handlebar.js` snippets that will get their context from the JSON at the URL defined in the `Widget`.
9. The above arrangement is all you need to make composite pages. There is room for improvement: For instance, the `gridster.js` that allows for drag-and-drop functionality does not currently serialize its state to the server. However, I intend to iron-out these niggles in the coming release.Watch this space.
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from mptt.managers import TreeManager
from django.template.defaultfilters import slugify


class Page(MPTTModel):
    '''
    A very simple Page model with gridster configurations.
    '''
    slug = models.SlugField(max_length=32)
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    in_navbar = models.BooleanField(default=True)
    parent = TreeForeignKey('self',
                            null=True,
                            blank=True,
                            related_name='children')
    # Now for gridster configuration
    # Ref: http://gridster.net/#documentation
    widget_margin_x = models.IntegerField(default=10)
    widget_margin_y = models.IntegerField(default=10)
    widget_base_dimension_x = models.IntegerField(default=100)
    widget_base_dimension_y = models.IntegerField(default=100)
    max_cols = models.IntegerField(default=16)
    min_cols = models.IntegerField(default=1)
    min_rows = models.IntegerField(default=16)
    max_size_x = models.IntegerField(default=16)
    max_size_y = models.IntegerField(default=16)
    # Widgets
    widgets = models.ManyToManyField('Widget')
    # MPTT TreeManager
    tree = TreeManager()

    class Meta:
        # This one is strictly for the future when we will
        # be required to control page level permissions.
        permissions = (("can_view", "Can view page"),)

    class MPTTMeta:
        # This is required for MPTT
        order_insertion_by = ['id']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        '''
        Overriding the save method to handle slugs and MPTT
        '''
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)
            # Take care of MPTT
            Page.tree.insert_node(self, self.parent)
        super(Page, self).save(*args, **kwargs)


class Widget(models.Model):
    '''
    A very simple Widget model with gridster configurations.
    '''
    slug = models.SlugField(max_length=64)
    title = models.CharField(max_length=64)
    url = models.URLField(blank=True)
    template = models.ForeignKey('Template', null=True, blank=True)
    # Now for widget configuration
    # Ref: http://gridster.net/#usage
    row = models.IntegerField(default=1)
    col = models.IntegerField(default=1)
    size_x = models.IntegerField(default=1)
    size_y = models.IntegerField(default=1)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        '''
        Overriding the save method to handle slugs
        '''
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify('widget-' + self.title)
        super(Widget, self).save(*args, **kwargs)


class Template(models.Model):
    '''
    Stores reusable templates. These templates are rendered
    using the handlebar client-side templating library.
    '''
    slug = models.SlugField(max_length=64)
    title = models.CharField(max_length=64)
    code = models.TextField()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        '''
        Overriding save to handle slugs.
        '''
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify('template-' + self.title)
        super(Template, self).save(*args, **kwargs)

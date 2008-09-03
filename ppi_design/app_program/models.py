from django.db import models
from django.contrib import admin
from ppi_design.app_basic.models import LanguageChoice


class CarBase(models.Model):
    """
        used mainly for the menu, this can either contain subcategories
        or it can be used to link to a single URL

        the order is how the program and it's submenus are displayed in under the main program category
    """
    name = models.CharField(max_length=200, unique=True);
    title = models.CharField(max_length=200) 
    order = models.IntegerField();
    url = models.URLField(blank=True);

    def __unicode__(self):
        return "[%s] %s" % (self.name, self.title)

    class Meta:
        verbose_name = "Program (top level menu)"
        verbose_name_plural = "Programs"

class CarSeries(models.Model):
    """
        title is what gets displayed in the menu, e.g. "2007+" or "SN 1998 2005+"
        order refers to the order for the menu within the Program
        program is the submenu the series belongs to
    """
    name = models.CharField(max_length=200, unique=True);
    title = models.CharField(max_length=200) 
    order = models.IntegerField();
    base = models.ForeignKey(CarBase)

    def __unicode__(self):
        return "[%s] %s"  % (self.name, self.title)

    class Meta:
        verbose_name = "Series (second level menu)"
        verbose_name_plural = "Series"


class Car(models.Model):
    """
        the name is the model name, e.g. "PPI RAZOR" or "TT S1"
        the order is for WITHIN the series
        series refers to a submenu for a program
    """
    name = models.CharField(max_length=200, unique=True) 
    title = models.CharField(max_length=200) 
    order = models.IntegerField();
    series = models.ForeignKey(CarSeries)
    store_url = models.URLField(blank=True);


    background_design = models.ImageField(upload_to='uploads/car/backgrounds')
    background_specs = models.ImageField(upload_to='uploads/car/backgrounds')
    background_gallery = models.ImageField(upload_to='uploads/car/backgrounds')

    def __Base__(self):
        return self.series.base

    def __unicode__(self):
        return "[%s] %s" % (self.name, self.title)


class Gallery(models.Model):
    CAR_THUMB_POSITIONS = ( 
                            (1, "Position 1"), 
                            (2, "Position 2"), 
                            (3, "Position 3"), 
                            (4, "Position 4"), 
                            (5, "Position 5"), 
                            (6, "Position 6"), 
                            (7, "Position 7"), 
                            (8, "Position 8"), 
                          )

    car = models.ForeignKey(Car)

    # this should be a choice of 1-8
    position = models.IntegerField(choices=CAR_THUMB_POSITIONS)

    thumb = models.ImageField(upload_to='uploads/car/gallery/thumb')
    large = models.ImageField(upload_to='uploads/car/gallery/large')

    def __unicode__(self):
        return 'image_' + self.car.name + '_pos_%i' % self.position 

    class Meta:
        ordering = ['position']


class Language(models.Model):

    car = models.ForeignKey(Car)

    language = models.ForeignKey(LanguageChoice)

    design_title = models.CharField(max_length=200)
    design_title_extra = models.CharField(max_length=200, blank=True)
    design_description = models.TextField()

    specs_title = models.CharField(max_length=200)
    specs_title_extra = models.CharField(max_length=200, blank=True)
    specs_description = models.TextField()

    gallery_title = models.CharField(max_length=200)
    gallery_title_extra = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
            return self.language.name

    class Meta:
        verbose_name = "Language Preferences"
        verbose_name_plural = "Language Preferences"


class Labels(models.Model):
    language = models.ForeignKey(LanguageChoice)

    design = models.CharField(max_length=100)
    specs = models.CharField(max_length=100)
    gallery = models.CharField(max_length=100)
    shop = models.CharField(max_length=100)

    def __unicode__(self):
        return self.language.name

    class Meta:
        verbose_name = "Label"
        verbose_name_plural = "Label Pages"

class LangInline(admin.StackedInline):
    model = Language 
    extra = 1
    max_num = 2

class GalleryInline(admin.TabularInline):
    model = Gallery 
    extra = 8
    max_num = 8


class CarBaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'order') 
    ordering = ['order']

class CarSeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'base', 'order')
    ordering = ['base', 'order']

class CarAdmin(admin.ModelAdmin):
    inlines = [GalleryInline, LangInline]
    list_display = ('title', '__Base__', 'series', 'order')
    ordering = ['series', 'order']

admin.site.register(Labels)
admin.site.register(CarBase, CarBaseAdmin)
admin.site.register(CarSeries, CarSeriesAdmin)
admin.site.register(Car, CarAdmin)

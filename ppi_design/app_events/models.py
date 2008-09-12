from django.db import models
from django.contrib import admin
from ppi_design.app_basic.models import LanguageChoice

# Create your models here.

class EventsLocation(models.Model):
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30, help_text="Make sure the country name is consistent.  Just use all lowercase.  Otherwise, you'll see the same country appearing twice in the menu, but with a slightly different spelling.")

    def __unicode__(self):
        return "%s, %s" % (self.city, self.country) 

class Events(models.Model):
    location = models.ForeignKey(EventsLocation)        
    title = models.CharField(max_length=30, help_text="Try to keep this language neutral, just the name of the event.")
    date = models.DateField(help_text="The events will be sorted by date, so this is important.  It will also be tacked onto the end of the title")

    def __unicode__(self):
        return "%s, (%s)" % (self.title, self.date)

class Gallery(models.Model):
    # currently I'm sticking with a total of 6 images per row, with 3 rows 
    GALLERY_NUM_ROW = 3
    GALLERY_NUM_COLS = 6
    GALLERY_THUMB_POSITIONS = ( 
                            (1, "Row 1, Col 1"), 
                            (2, "Row 1, Col 2"), 
                            (3, "Row 1, Col 3"), 
                            (4, "Row 1, Col 4"), 
                            (5, "Row 1, Col 5"), 
                            (6, "Row 1, Col 6"), 

                            (7, "Row 2, Col 1"), 
                            (8, "Row 2, Col 2"), 
                            (9, "Row 2, Col 3"), 
                            (10, "Row 2, Col 4"), 
                            (11, "Row 2, Col 5"), 
                            (12, "Row 2, Col 6"), 

                            (13, "Row 3, Col 1"), 
                            (14, "Row 3, Col 2"), 
                            (15, "Row 3, Col 3"), 
                            (16, "Row 3, Col 4"), 
                            (17, "Row 3, Col 5"), 
                            (18, "Row 3, Col 6"), 
                          )

    GALLERY_ROWS = (
                    (1, "Row 1"),
                    (2, "Row 2"),
                    (3, "Row 3"),
                    )
    GALLERY_COLS = (
                    (1, "Col 1"), 
                    (2, "Col 2"), 
                    (3, "Col 3"), 
                    (4, "Col 4"), 
                    (5, "Col 5"), 
                    (6, "Col 6"), 
                    )

    event = models.ForeignKey(Events)
    row = models.IntegerField(choices=GALLERY_ROWS)
    col = models.IntegerField(choices=GALLERY_COLS)

    thumb = models.ImageField(upload_to='uploads/events/gallery/thumb')
    large = models.ImageField(upload_to='uploads/events/gallery/large')

    def __unicode__(self):
        return "[%s,%s]image(%i,%i)" % (self.event.title, self.event.date, self.row, self.col)

    class Meta:
        ordering = ['row', 'col']


class LanguageEvent(models.Model):
    event = models.ForeignKey(Events)
    language = models.ForeignKey(LanguageChoice)
    description = models.TextField(blank=True, help_text="this is just meant as a short description for the event.  The shorter, the better")

    def __unicode__(self):
            return self.language.name

    class Meta:
        verbose_name = "Language Preferences"
        verbose_name_plural = "Language Preferences"


class LangInline(admin.StackedInline):
    model = LanguageEvent 
    extra = 1
    max_num = 2

class GalleryInline(admin.TabularInline):
    model = Gallery 
    extra = 6 
    max_num = 18 

class EventsAdmin(admin.ModelAdmin):
    inlines = [GalleryInline, LangInline]
    #list_display = ('title', '__Base__', 'series', 'order')
    #ordering = ['series', 'order']

admin.site.register(EventsLocation)
admin.site.register(Events,EventsAdmin)

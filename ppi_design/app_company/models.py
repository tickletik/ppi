from django.db import models
from django.contrib import admin
import datetime
from ppi_design.app_basic.models import LanguageChoice 

class CompanyPage(models.Model):
    name = models.CharField(max_length=200)
    order = models.IntegerField()

    def __unicode__(self):
        return self.name

class LanguagePref(models.Model):
    """
        company - foreign key to a single description of the particular company page
        language - tells us which language this is in 
        menu - the label we'll see on the drop down menu
        title - header in the page itself, don't fold this into description.  As it is, that shouldn't be there 
        description - really bad code used to store marked up text.  very bad idea. any programmer
           who wants to scrap this and put normal fields in has my blessing. just tell me how you
           managed to convince Ben to go along with it.
    """

    company = models.ForeignKey(CompanyPage)
    language = models.ForeignKey(LanguageChoice)

    menu = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField()

    def __unicode__(self):
            return self.language.name

    class Meta:
        verbose_name = "Language Preferences"
        verbose_name_plural = "Language Preferences"

class LangInline(admin.StackedInline):
    model = LanguagePref 
    extra = 1
    max_num = 2

class CompanyPageAdmin(admin.ModelAdmin):
    inlines = [LangInline]
    list_display = ('name', 'order')

admin.site.register(CompanyPage, CompanyPageAdmin)


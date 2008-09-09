from django.db import models
from django.contrib import admin
from ppi_design.settings import LANGUAGE_CHOICES

def _language(code):
    """
    helper function to get the language choices out of the settings file
    """

    lan = 'ERROR in LANGUAGE_CHOICES' 
    for e in enumerate(LANGUAGE_CHOICES):
        if code in e[1]:
            lan = e[1][1]
    return lan


# Create your models here.
class LanguageChoice(models.Model):
    # probably redundent to put language choices in here, but what the hell        
    name = models.CharField(max_length=40)
    code = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    image = models.ImageField(upload_to='uploads/flag')
    menu_order = models.IntegerField()

    # necessary for if we're going to use this language
    activated = models.BooleanField()

    def __unicode__(self):
        return "[%s] %s" % (self.code, self.name)

class Internationalization(models.Model):
    language = models.ForeignKey(LanguageChoice)
    lang_selection = models.CharField(max_length=60)

    menu_home = models.CharField(max_length=20)
    menu_company = models.CharField(max_length=20)
    menu_program = models.CharField(max_length=20)
    menu_shop = models.CharField(max_length=20)
    menu_events = models.CharField(max_length=20)
    menu_press = models.CharField(max_length=20)
    menu_news = models.CharField(max_length=20)
    menu_contact = models.CharField(max_length=20)

    contact_manufacturer = models.CharField(max_length=20)
    contact_distributor = models.CharField(max_length=20)

    press_publications = models.CharField(max_length=30)
    press_photographers = models.CharField(max_length=30)
    press_login = models.CharField(max_length=30)

    def __unicode__(self):
        return "[%s] %s" % (self.language.code, self.language.name)

admin.site.register(LanguageChoice)
admin.site.register(Internationalization)

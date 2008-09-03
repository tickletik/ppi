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

    def __unicode__(self):
        return "[" + self.code+ "] " + self.name

admin.site.register(LanguageChoice)
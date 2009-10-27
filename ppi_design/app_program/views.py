from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import HttpResponse
from ppi_design.app_program.models import *
from ppi_design.app_basic.models import LanguageChoice
from ppi_design.settings import MEDIA_URL

import libxml2
import libxslt
import re


def _xml_labels(code):
    language = LanguageChoice.objects.get(code=code) 
    l = Labels.objects.get(language=language)
    t = loader.get_template('program/labels.xml')
    c = Context({'l':l,})
    return t.render(c)

def _xml_background_urls(_name):
    car = Car.objects.get(name=_name)
    t = loader.get_template('program/urls_background.xml')
    c = Context({'MEDIA_URL':MEDIA_URL, 'car':car,})
    return t.render(c)

def _xml_gallery_urls(_name):
    car = Car.objects.get(name=_name)
    gallery = Gallery.objects.filter(car=car)
    t = loader.get_template('program/urls_gallery.xml')
    c = Context({'MEDIA_URL':MEDIA_URL, 'gallery':gallery,})
    return t.render(c)

def _xml_info(code, _name):
    language = LanguageChoice.objects.get(code=code) 
    car = Car.objects.get(name=_name)
    info = Language.objects.get(car=car, language=language) 
    
    #pattern_amp = re.compile(' & ', re.I|re.M)
    #pattern = re.compile('\r\n', re.I|re.M)
    #info.design_description = unicode(pattern.sub("\n", info.design_description))
    #info.specs_description = unicode(pattern.sub("\n", info.specs_description))

    t = loader.get_template("xslt/company.xslt")
    c = Context({})
    xslt = libxslt.parseStylesheetDoc(libxml2.parseDoc(t.render(c)))


    desc = dict()

    doc = "<%s>%s</%s>" % ("program", info.specs_description, "program") 
    doc = libxml2.parseDoc(doc.encode("utf-8"))
    res = libxslt.stylesheet.applyStylesheet(xslt, doc, {})
    desc["specs"] = res.__str__()

    doc = "<%s>%s</%s>" % ("program", info.design_description, "program") 
    doc = libxml2.parseDoc(doc.encode("utf-8"))
    res = libxslt.stylesheet.applyStylesheet(xslt, doc, {})
    desc["design"] = res.__str__()


    p = re.compile('<\?xml version="1.0"\?>')
    desc["specs"] = p.sub("", desc["specs"])
    desc["design"] = p.sub("", desc["design"])


    t = loader.get_template("program/data.xml")
    c = Context({"info":info, "description":desc})
    return t.render(c)

def http_labels(request, lang):
    return HttpResponse(_xml_labels(lang))

def http_backgrounds(request, lang, _name):
    return HttpResponse(_xml_background_urls(_name))

def http_info(request, lang, _name):
    return HttpResponse(_xml_info(lang, _name)) 

def http_gallery(request, _name):
    return HttpResponse(_xml_gallery_urls(_name))


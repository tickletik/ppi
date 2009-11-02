from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import HttpResponse
from ppi_design.app_company.models import * 
from ppi_design.app_basic.models import LanguageChoice

import libxml2
import libxslt
import re


def _xml_company_text(code, name):
    company = CompanyPage.objects.get(name=name)
    language = LanguageChoice.objects.get(code=code)
    pref = LanguagePref.objects.get(company=company, language=language)

    t = loader.get_template("xslt/company.xslt")
    c = Context({})
    xslt = libxslt.parseStylesheetDoc(libxml2.parseDoc(t.render(c)))

    doc = "<%s>%s</%s>" % ("company", pref.description, "company") 
    doc = libxml2.parseDoc(doc.encode("utf-8"))
    res = libxslt.stylesheet.applyStylesheet(xslt, doc, {})
    content = res.content

    """
    I don't know how to remove the stupid declaration yet, and I need
    this up and running today.  Figure it out later and get rid of this
    """

    p = re.compile('<\?xml version="1.0"\?>')
    content = p.sub("", content)


    info = dict()
    info['title'] = pref.title
    info['description'] = content 

    t = loader.get_template('company/content.xml')
    c = Context({'language':info,})
    return t.render(c)

def http_text(request, lang, name):
    return HttpResponse(_xml_company_text(lang, name))

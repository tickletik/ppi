from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import HttpResponse
from ppi_design.app_company.models import * 
from ppi_design.app_basic.models import LanguageChoice

def _xml_company_text(code, name):
    company = CompanyPage.objects.get(name=name)
    language = LanguageChoice.objects.get(code=code)
    pref = LanguagePref.objects.get(company=company, language=language)
    t = loader.get_template('company/content.xml')
    c = Context({'language':pref,})
    return t.render(c)

def http_text(request, lang, name):
    return HttpResponse(_xml_company_text(lang, name))

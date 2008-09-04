from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import HttpResponse
import ppi_design.app_company.models as c_models 
from ppi_design.app_basic.models import *


def _xml_menu(lang):

    company_pages = c_models.CompanyPage.objects.order_by('order')    
    c_menus = [_get_comp_lang(comp, lang) for comp in company_pages]
         
    t = loader.get_template('basic/menu.xml')
    c = Context({'company_list':c_menus})
    return t.render(c)

def _get_comp_lang(company, code):
    language = LanguageChoice.objects.get(code=code) 
    pref = c_models.LanguagePref.objects.get(company=company, language=language)
    return {'title':pref.menu, 'name':company.name}

def http_menu(request, lang):
    return HttpResponse(_xml_menu(lang))

def http_index(request):
    t = loader.get_template('basic/index.html')
    c = Context({})
    return HttpResponse(t.render(c))

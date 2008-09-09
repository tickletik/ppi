from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import HttpResponse

import ppi_design.app_company.models as c_models 
import ppi_design.app_program.models as p_models 

from ppi_design.app_basic.models import *
from ppi_design.settings import MEDIA_URL, BASE_URL


def _xml_menu_program(code):
    language = LanguageChoice.objects.get(code=code)
    base = p_models.CarBase.objects.all()

    program = list() 
    for b in base:
            series = p_models.CarSeries.objects.filter(base=b)
            series_list = list()
            for s in series:
                cars = p_models.Car.objects.filter(series=s)
                car_list = list()
                for c in cars:
                        car_list.append(c)

                series_list.append({"series":s, "cars":car_list})
            program.append({"base":b, "series":series_list})

    t = loader.get_template("basic/menu.xml")
    c = Context({"program":program})
    return t.render(c)


def _xml_menu(lang):
    language = LanguageChoice.objects.get(code=lang)
    labels = Internationalization.objects.get(language=language)

    # create the company page drop down menu list
    company_pages = c_models.CompanyPage.objects.order_by("order")    
    c_menus = [_get_comp_lang(comp, lang) for comp in company_pages]

    # create the program drop down menu list
    base = p_models.CarBase.objects.all()
    program = list() 
    for b in base:
            series = p_models.CarSeries.objects.filter(base=b)
            series_list = list()
            for s in series:
                cars = p_models.Car.objects.filter(series=s)
                car_list = list()
                for c in cars:
                        car_list.append(c)

                series_list.append({"series":s, "cars":car_list})
            program.append({"base":b, "series":series_list})

    t = loader.get_template("basic/menu.xml")
    c = Context({"company_list":c_menus, "program":program, "labels":labels})
    return t.render(c)


def _xml_languages():
    languages = LanguageChoice.objects.order_by("menu_order")

    t = loader.get_template("basic/urls_languages.xml")
    c = Context({"MEDIA_URL":MEDIA_URL, "languages":languages})
    return t.render(c)


def _xml_international(code):
    language = LanguageChoice.objects.get(code=code)
    international = Internationalization.objects.get(language=language)
    t = loader.get_template("basic/international.xml")
    c = Context({"international":international})
    return t.render(c)


def _get_comp_lang(company, code):
    language = LanguageChoice.objects.get(code=code) 
    pref = c_models.LanguagePref.objects.get(company=company, language=language)
    return {"title":pref.menu, "name":company.name}


def http_internationalization(request, code):
    return HttpResponse(_xml_international(code))


def http_languages(request):
    return HttpResponse(_xml_languages())


def http_menu(request, lang):
    return HttpResponse(_xml_menu(lang))


def http_index(request):
    t = loader.get_template("basic/index.html")
    c = Context({"MEDIA_URL":MEDIA_URL, "BASE_URL":BASE_URL})
    return HttpResponse(t.render(c))


def http_menu_program(request, lang):
    return HttpResponse(_xml_menu_program(lang))

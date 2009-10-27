from pyamf.remoting.gateway.django import DjangoGateway
import elementtree.ElementTree as ET
import re

# test the branching and mergining of git

import ppi_design.app_program.views as program 


def get_program(request, params):

    lang = params["_lang"]
    _name = params["_car"] 

    dom_labels = ET.fromstring(program._xml_labels(lang).encode("utf-8"))
    dom_backgrounds = ET.fromstring(program._xml_background_urls(_name).encode("utf-8"))
    dom_gallery = ET.fromstring(program._xml_gallery_urls(_name).encode("utf-8"))
    dom_info = ET.fromstring(program._xml_info(lang, _name).encode("utf-8"))
    

    car_dict = dict()
    car_dict["labels"] = dom_labels
    car_dict["backgrounds"] = dom_backgrounds
    car_dict["info"] = dom_info
    car_dict["gallery"] = dom_gallery
    

    return car_dict 


services = {
    "program" : get_program,
}

ppi_gateway = DjangoGateway(services)

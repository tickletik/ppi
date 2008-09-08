from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('ppi_design.app_company.views',
    # Example:
    (r'^xml/company/info/(?P<lang>\D{2})/(?P<name>\w+)/$', 'http_text'),
)

urlpatterns += patterns('ppi_design.app_basic.views',
    (r'^$', 'http_index'),
    (r'^xml/menu/(?P<lang>\D{2})/$', 'http_menu'),
    (r'^xml/language/urls/$', 'http_languages'),
    (r'^xml/language/labels/(?P<code>\D{2})/$', 'http_internationalization'),
)

urlpatterns += patterns('ppi_design.app_program.views',
    (r'^programs/(?P<lang>\D{2})/labels/$', 'http_labels'),
    (r'^programs/(?P<lang>\D{2})/(?P<_name>\w+)/backgrounds/$', 'http_backgrounds'),
    (r'^programs/(?P<lang>\D{2})/(?P<_name>\w+)/info/$', 'http_info'),
    (r'^programs/(?P<_name>\w+)/gallery/$', 'http_gallery'),
)

urlpatterns += patterns('', 

    (r'^gateway/', 'ppi_design.amfgateway.ppi_gateway'),
    (r'^admin/(.*)', admin.site.root), 
)

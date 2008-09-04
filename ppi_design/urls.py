from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('ppi_design.app_company.views',
    # Example:
    (r'^company/(?P<lang>\D{2})/(?P<name>\w+)/text/$', 'http_text'),
)

urlpatterns += patterns('ppi_design.app_basic.views',
    (r'^$', 'http_index'),
    (r'^main/(?P<lang>\D{2})/menu/$', 'http_menu'),
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

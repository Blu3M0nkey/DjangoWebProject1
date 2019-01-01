"""
Definition of urls for DjangoWebProject1.

contains a table of contents for the Django project, which you also modify in the course of development.
"""

from django.conf.urls import include, url
import helloDjApp.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', DjangoWebProject1.views.home, name='home'),
    # url(r'^DjangoWebProject1/', include('DjangoWebProject1.DjangoWebProject1.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', helloDjApp.views.index, name='index'),
    url(r'^home$', helloDjApp.views.index, name='home'),
    url(r'^about$', helloDjApp.views.about, name='about'),

]

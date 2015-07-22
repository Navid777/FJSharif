"""FJSharif URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from FJSharif import settings
from PatientReport import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', views.login, name='login'),
    url(r'^create/surgeon/$', views.create_surgeon),
    url(r'^create/proficiency/$', views.create_proficiency),
    url(r'^create/alignment_parameter_name/$', views.create_alignment_parameter_name),
    url(r'^create/patient/$', views.create_patient),
    url(r'^create/staff$', views.create_staff),
    url(r'^edit/proficiency/(?P<proficiency_id>\d+)$', views.edit_proficiency),
    url(r'^edit/alignment_parameter_name/(?P<alignment_parameter_name_id>\d+)$', views.edit_alignment_parameter_name),
    url(r'^edit/patient/(?P<patient_id>\d+)$', views.edit_patient),
    url(r'^edit/surgeon/(?P<surgeon_id>\d+)$', views.edit_surgeon),
    url(r'^edit/staff/(?P<staff_id>\d+)$', views.edit_staff),
    url(r'^home$', views.home, name='home'),
    url(r'^view/patient/(?P<patient_id>\d+)$', views.view_patient, name='view_patient'),
    url(r'^view/order/(?P<order_id>\d+)$', views.view_order, name='view_order'),
    url(r'^test$', views.test),
]

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT,
                            }),
                            )

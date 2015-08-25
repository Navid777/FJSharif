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
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^create/surgeon/$', views.create_surgeon, name='create_surgeon'),
    url(r'^create/proficiency/$', views.create_proficiency, name='create_proficiency'),
    url(r'^create/alignment_parameter_name/$', views.create_alignment_parameter_name,
        name='create_alignment_parameter_name'),
    url(r'^create/patient/$', views.create_patient, name='create_patient'),
    url(r'^create/staff$', views.create_staff, name='create_staff'),
    url(r'^create/report$', views.create_report, name='create_report'),
    url(r'^edit/proficiency/(?P<proficiency_id>\d+)$', views.edit_proficiency, name='edit_proficiency'),
    url(r'^edit/alignment_parameter_name/(?P<alignment_parameter_name_id>\d+)$', views.edit_alignment_parameter_name,
        name='edit_alignment_parameter_name'),
    url(r'^create/order$', views.create_order, name='create_order'),
    url(r'^create/order/(?P<patient_id>\d+)$', views.create_order, name='create_order'),
    url(r'^create/order/(?P<patient_id>\d+)/(?P<surgeon_id>\d+)$', views.create_order, name='create_order'),
    url(r'^edit/patient/(?P<patient_id>\d+)$', views.edit_patient, name='edit_patient'),
    url(r'^edit/surgeon/(?P<surgeon_id>\d+)$', views.edit_surgeon, name='edit_surgeon'),
    url(r'^edit/staff/(?P<staff_id>\d+)$', views.edit_staff, name='edit_staff'),
    url(r'^home$', views.home, name='home'),
    url(r'^view/patients/(?P<surgeon_id>\d+)$', views.view_patients, name='view_patients'),
    url(r'^view/patient/(?P<patient_id>\d+)$', views.view_patient, name='view_patient'),
    url(r'^view/report/(?P<order_id>\d+)$', views.view_report, name='view_report'),
    url(r'^view/guides/(?P<order_id>\d+)$', views.view_guides, name='view_guides'),
    url(r'^view/pre_plannings/(?P<order_id>\d+)$', views.view_pre_plannings, name='view_pre_plannings'),
    url(r'^test$', views.test),
    url(r'^manage/patients$', views.manage_patients, name='manage_patients'),
    url(r'^manage/patients/(?P<page_num>\d+)$', views.manage_patients, name='manage_patients'),
    url(r'^manage/surgeons$', views.manage_surgeons, name='manage_surgeons'),
    url(r'^manage/surgeons/(?P<page_num>\d+)$', views.manage_surgeons, name='manage_surgeons'),
    url(r'^manage/proficiencies$', views.manage_proficiencies, name='manage_proficiencies'),
    url(r'^manage/orders$', views.manage_orders, name='manage_orders'),
    url(r'^manage/alignment_parameter_names$', views.manage_alignment_parameter_names,
        name='manage_alignment_parameter_names'),
    url(r'^ajax/delete/patient/(?P<patient_id>\d+)$', views.ajax_delete_patient),
    url(r'^ajax/delete/surgeon/(?P<surgeon_id>\d+)$', views.ajax_delete_surgeon),
    url(r'^ajax/delete/alignment_parameter_name/(?P<parameter_id>\d+)$', views.ajax_delete_alignment_parameter_name),
]

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT,
                            }),
                            )

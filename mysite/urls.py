from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from mysite.views import viewsModule

urlpatterns = patterns('',
    # Examples:
    url(r'^$', viewsModule.index, name='index'),
    url(r'^linkedin_login/', 'mysite.views.linkedin', 'login'),
	
    url(r'^doctor/(?P<doctor_id>\d+)$', viewsModule.show_doctor, name='show_doctor'),
	
    url(r'^publish_case$', viewsModule.publish_case, name='publish_case'),
	
    url(r'^admin/', include(admin.site.urls)),
)
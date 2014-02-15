from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
admin.autodiscover()

from mysite.views import viewsModule
from mysite.views import linkedinModule

urlpatterns = patterns('',
    # Examples:
    url(r'^$', viewsModule.index, name='index'),
    url(r'^linkedin_login$', linkedinModule.login, name='login'),	
    url(r'^doctor/(?P<doctor_id>\d+)$', viewsModule.show_doctor, name='show_doctor'),
	
    url(r'^publish_case$', viewsModule.publish_case, name='publish_case'),
	
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [

	url(r'^$', 'newsletter.views.home', name='home'),
	url(r'^contact/$', 'newsletter.views.contact', name='contact'),
	url(r'^about/$', 'src.views.about', name='about'),
	url(r'^notes/$', 'src.views.notes', name='notes'),
	url(r'^upload/$', 'src.views.upload', name='upload'),
	
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

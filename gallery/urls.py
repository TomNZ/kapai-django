from django.conf.urls.defaults import *

urlpatterns = patterns('kapai_django.gallery.views',
	(r'^upload/$', 'upload'),
	(r'^(?P<slug>\w+)/$', 'viewgallery'),
	(r'^$', 'index'),
)
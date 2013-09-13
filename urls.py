from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
(r'^progression/', include('kapai_django.progression.urls')),
(r'^gallery/', include('kapai_django.gallery.urls')),
(r'^raid/', include('kapai_django.raidtool.urls')),
(r'^admin/', include(admin.site.urls)),
#(r'^admin$', 'django.contrib.admin.site.index')),
(r'^accounts/login/$', 'django.contrib.auth.views.login'),
(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
(r'^', include('kapai_django.index.urls')),
)

handler404 = 'kapai_django.index.views.custom404'

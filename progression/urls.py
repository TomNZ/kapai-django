from django.conf.urls.defaults import *

urlpatterns = patterns('kapai_django.progression.views',
	(r'^json/boss/by_instance/(?P<instance_id>\d+)/$', 'json_get_bosses_by_instance'),
	(r'^json/boss_detail/by_boss/(?P<boss_id>\d+)/$', 'json_get_bossdetails_by_boss'),
	(r'^$', 'index'),
)
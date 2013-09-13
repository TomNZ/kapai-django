from django.conf.urls.defaults import *

urlpatterns = patterns('kapai_django.raidtool.views',
	(r'^char/(?P<char_id>\d+)/$', 'char_view'),
	(r'^char/(?P<char_id>\d+)/edit/$', 'char_edit'),
	(r'^char/(?P<char_id>\d+)/edit-encounters/$', 'char_edit_encounters'),
	(r'^char/new/$', 'char_new'),
	(r'^lead/list/$', 'lead_list'),
	(r'^admin/char/list/$', 'admin_char_list'),
	(r'^import/epgp/$', 'import_epgp'),
	(r'^json/char_boss/(?P<charboss_id>\d+)/delete/$', 'json_delete_charboss'),
	(r'^$', 'index'),
)
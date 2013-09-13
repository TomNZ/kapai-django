from django.shortcuts import render_to_response
from kapai_django.classes import KapaiContext
from kapai_django.progression.models import *
from django.core import serializers
from django.http import HttpResponse

def index(request):
	return render_to_response('progression/index.html', {'show_side_recruitment': True}, context_instance=KapaiContext(request))

def json_get_bosses_by_instance(request, instance_id):
	instance = Instance.objects.get(pk=instance_id)
	bosses = Boss.objects.get_by_instance(instance)

	return HttpResponse(serializers.serialize('json', bosses, fields=('name')), mimetype='application/javascript')

def json_get_bossdetails_by_boss(request, boss_id):
	boss = Boss.objects.get(pk=boss_id)
	bossdetails = BossDetail.objects.get_by_boss(boss)
	
	return HttpResponse(serializers.serialize('json', bossdetails, fields=('name')), mimetype='application/javascript')
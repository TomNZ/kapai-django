import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.db.models import Q
from django.forms.models import modelformset_factory
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.utils.functional import curry, wraps
from kapai_django.classes import KapaiContext, DataImport
from kapai_django.raidtool.models import *
from kapai_django.raidtool.forms import *
from kapai_django.progression.models import Instance

def is_raid_leader(user):
	return user.is_staff or user.get_profile().raid_leader

def is_raid_admin(user):
	return user.is_staff or user.get_profile().raid_admin

def get_raid_members(raid):
	raid_chars = Character.objects.filter(raidchar__in=RaidChar.objects.filter(raid=raid))
	if not raid_chars or raid_chars.count() == 0:
		raid_chars = Character.objects.get_active()
	return raid_chars
	
def clear_raid_members(raid):
	raid.raidchar_set.all().delete()

def get_raid(request):
	raid_id = request.session.get('raid_id')
	raid = None
	if raid_id:
		raid = Raid.objects.get(pk=raid_id)
		elapsed = datetime.datetime.now() - raid.raid_date
		expired = elapsed > datetime.timedelta(hours=4)
	if not raid or raid.user <> request.user or expired:
		raid = Raid(user=request.user, raid_date=datetime.datetime.now())
		raid.save()
		request.session['raid_id'] = raid.pk
	else:
		raid.raid_date = datetime.datetime.now()
		raid.save()
	return raid

@login_required
def index(request):
	raid_leader = is_raid_leader(request.user)
	raid_admin = is_raid_admin(request.user)
	chars = request.user.character_set.get_active()
	return render_to_response('raidtool/index.html', {'chars': chars, 'raid_leader': raid_leader, 'raid_admin': raid_admin}, context_instance=KapaiContext(request))

@login_required
def lead_list(request):
	is_leader = is_raid_leader(request.user)
	is_admin = is_raid_admin(request.user)
	if not is_leader:
		return render_to_response('404.html', {}, context_instance=KapaiContext(request))
	
	raid = get_raid(request)
	
	# Filters
	ranks = ['R', 'T', 'S', 'A']
	instance = None
		
	if request.POST:
		filter_form = LeadListFilterForm(request.POST)
		if filter_form.is_valid():
			filter_ranks = filter_form.cleaned_data.get('ranks')
			if filter_ranks:
				ranks = filter_ranks
			raid_data = filter_form.cleaned_data.get('raid_data')
			instance = filter_form.cleaned_data.get('instance')
			if raid_data and raid_data <> '':
				dataimport = DataImport()
				dataimport.process_raid_list(raid, raid_data)
				post = request.POST.copy()
				del post['raid_data']
				filter_form = LeadListFilterForm(post)
			if 'submit-clear' in request.POST:
				clear_raid_members(raid)
				
	else:
		filter_form = LeadListFilterForm()
		
	raid_chars = get_raid_members(raid).filter(Q(rank__in=ranks) | Q(rank=None))
	char_count = len(raid_chars)
	char_bosses = CharacterBoss.objects.get_active().filter(char__in=raid_chars)
	
	if instance:
		char_bosses = char_bosses.filter(boss__instance=instance)

	return render_to_response('raidtool/lead_list.html', {'char_bosses': char_bosses, 'filter_form': filter_form, 'char_count': char_count, 'is_leader': is_leader, 'is_admin': is_admin}, context_instance=KapaiContext(request))	
	
@login_required
def admin_char_list(request):
	if not is_raid_admin(request.user):
		return render_to_response('404.html', {}, context_instance=KapaiContext(request))

	chars = Character.objects.get_active()
	return render_to_response('raidtool/admin_char_list.html', {'chars': chars}, context_instance=KapaiContext(request))

@login_required
def import_epgp(request):
	if not is_raid_admin(request.user):
		return render_to_response('404.html', {}, context_instance=KapaiContext(request))
	
	result = None
	
	if request.method == 'POST':
		data = request.POST['epgp_data']
		if data:
			dataimport = DataImport()
			num_processed = dataimport.process_epgp_data(data)
			result = "Success: " + `num_processed` + " characters processed"
	
	return render_to_response('raidtool/import_epgp.html', {'result': result}, context_instance=KapaiContext(request))

@login_required
def char_view(request, char_id):
	try:
		if is_raid_admin(request.user):
			char = Character.objects.get(pk=char_id)
		else:
			char = request.user.character_set.get(pk=char_id)
	except ObjectDoesNotExist:
		return render_to_response('raidtool/invalid_char.html', context_instance=KapaiContext(request))
	
	return render_to_response('raidtool/char_view.html', {'char': char}, context_instance=KapaiContext(request))

@login_required
def char_edit(request, char_id):
	try:
		if is_raid_admin(request.user):
			char = Character.objects.get(pk=char_id)
		else:
			char = request.user.character_set.get(pk=char_id)
	except ObjectDoesNotExist:
		return render_to_response('raidtool/invalid_char.html', context_instance=KapaiContext(request))
	
	if request.method == 'POST': # Form has been submitted
		form = CharacterForm(request.POST, instance=char)
		if form.is_valid():
			form.save()
			viewurl = reverse('kapai_django.raidtool.views.char_view', kwargs={'char_id': char.pk})
			return HttpResponseRedirect(viewurl)

	else:
		form = CharacterForm(instance=char)
	
	return render_to_response('raidtool/char_edit.html', {'form': form, 'char': char}, context_instance=KapaiContext(request))

@login_required
def char_edit_encounters(request, char_id):
	try:
		if is_raid_admin(request.user):
			char = Character.objects.get(pk=char_id)
		else:
			char = request.user.character_set.get(pk=char_id)
	except ObjectDoesNotExist:
		return render_to_response('raidtool/invalid_char.html', context_instance=KapaiContext(request))

	result = None
	instances = Instance.objects.get_current()
	forms = {}
	
	if request.method == 'POST': # Form has been submitted
		for instance in instances:
			CharacterBossFormSet = modelformset_factory(CharacterBoss, form=make_characterboss_form(instance), extra=3, can_delete=True)
			forms[instance] = CharacterBossFormSet(request.POST, queryset=char.characterboss_set.get_by_instance(instance), prefix='i'+`instance.pk`)
			if forms[instance].is_valid():
				if not result:
					result = "Save successful."
					
				char_bosses = forms[instance].save(commit=False)
				# Save existing/new
				char_boss_ids = []
				for char_boss in char_bosses:
					char_boss.char = char
					try:
						char_boss.save()
						char_boss_ids.append(char_boss.pk)
					except IntegrityError:
						pass
				forms[instance] = CharacterBossFormSet(queryset=char.characterboss_set.get_by_instance(instance), prefix='i'+`instance.pk`)
			else:
				if not result:
					result = "Warning: Some fields are incorrect, please check your input."
	else:
		for instance in instances:
			CharacterBossFormSet = modelformset_factory(CharacterBoss, form=make_characterboss_form(instance), extra=3, can_delete=True)
			forms[instance] = CharacterBossFormSet(queryset=char.characterboss_set.get_by_instance(instance), prefix='i'+`instance.pk`)
	
	return render_to_response('raidtool/char_edit_encounters.html', {'forms': forms, 'char': char, 'instances': instances, 'result': result}, context_instance=KapaiContext(request))

@login_required
def char_new(request):
	if request.method == 'POST': # Form has been submitted
		if 'submit-claim' in request.POST:		
			claim_form = CharacterSelectForm(request.POST)
			create_form = CharacterForm()
			if claim_form.is_valid():
				char = claim_form.cleaned_data['char']
				char.user = request.user
				char.save()
				editurl = reverse('kapai_django.raidtool.views.char_edit', kwargs={'char_id': char.pk})
				return HttpResponseRedirect(editurl)
		
		if 'submit-create' in request.POST:
			create_form = CharacterForm(request.POST)
			claim_form = CharacterSelectForm()
			if create_form.is_valid():
				char = create_form.save()
				char.user = request.user
				char.save()
				indexurl = reverse('kapai_django.raidtool.views.index')
				return HttpResponseRedirect(indexurl)
	else:
		claim_form = CharacterSelectForm()
		create_form = CharacterForm()
	
	return render_to_response('raidtool/char_new.html', {'create_form': create_form, 'claim_form': claim_form}, context_instance=KapaiContext(request))

@login_required
def json_delete_charboss(request, charboss_id):
	if not is_raid_admin(request.user):
		return render_to_response('404.html', {}, context_instance=KapaiContext(request))
	
	char_boss = CharacterBoss.objects.get(pk=charboss_id)
	char_boss.delete()
	
	return HttpResponse('{ "success": true }', mimetype='application/javascript')
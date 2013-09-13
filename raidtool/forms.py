from django.forms import Form, ModelForm, Select, CharField, TextInput, ModelChoiceField, ValidationError, MultipleChoiceField, CheckboxSelectMultiple, Textarea
from django.forms.formsets import formset_factory
from kapai_django.raidtool.models import Character, CharacterBoss, ROLE_CHOICES, RANK_CHOICES
from kapai_django.progression.models import Instance, Boss, BossDetail

class ModelNameChoiceField(ModelChoiceField):
	def label_from_instance(self, obj):
		return obj.name

class LeadListFilterForm(Form):
	instance = ModelNameChoiceField(queryset=Instance.objects.get_current(), required=False)
	ranks = MultipleChoiceField(choices=RANK_CHOICES, required=True, initial=['R', 'T', 'S', 'A'], widget=CheckboxSelectMultiple)
	raid_data = CharField(required=False, widget=Textarea, label='Raid list import')

class CharacterForm(ModelForm):
	class Meta:
		model = Character
		fields = ('name', 'char_class', 'rank', 'main_role')

class CharacterSelectForm(Form):
	char = ModelChoiceField(queryset=Character.objects.get_unclaimed(), label='Name')

def make_characterboss_form(instance):
	class CharacterBossForm(ModelForm):
		boss = ModelNameChoiceField(queryset=Boss.objects.filter(instance=instance, active=True, is_encounter=True).order_by('ordering'), widget=Select(attrs={'style': 'width: 150px', 'class': 'boss-edit'}))
		boss_detail = ModelChoiceField(queryset=BossDetail.objects.filter(boss__in=Boss.objects.filter(instance=instance, active=True, is_encounter=True)).order_by('ordering'), required=False, label='Encounter', empty_label='Normal mode', widget=Select(attrs={'style': 'width: 150px', 'class': 'boss-detail-edit'}))
		notes = CharField(required=False, widget=TextInput(attrs={'style': 'width: 80px'}))
		
		def clean_boss_detail(self):
			boss_detail = self.cleaned_data.get('boss_detail')
			
			if self.cleaned_data.has_key('boss'):
				boss = self.cleaned_data['boss']
				if boss_detail and boss_detail not in boss.bossdetail_set.all():
					raise ValidationError("Selected encounter is not valid for the selected boss.")
			
			return boss_detail
		
		class Meta:
			model = CharacterBoss
			fields = ('boss', 'boss_detail', 'notes')
	return CharacterBossForm
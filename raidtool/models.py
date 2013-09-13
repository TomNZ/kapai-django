import datetime
from django.db import models
from kapai_django.recruitment.models import RecruitmentClass
from kapai_django.progression.models import Boss, BossDetail, Instance
from kapai_django.index.models import Settings
from django.contrib.auth.models import User

ROLE_CHOICES = (
	('T', 'Tank'),
	('H', 'Healer'),
	('D', 'Damage'),
)

class CharacterRole(models.Model):
	"""Describes a character's role in the raid"""
	
	name = models.CharField(max_length=50)
	role = models.CharField(max_length=1, choices=ROLE_CHOICES)

	def __unicode__(self):
		return self.name

RANK_CHOICES = (
	('R', 'Raider'),
	('T', 'Trial'),
	('S', 'Social Member'),
	('A', 'Alt'),
)

class CharacterManager(models.Manager):
	use_for_related_fields = True
	
	def get_active(self):
		return self.filter(active=True).order_by('name')
	
	def get_unclaimed(self):
		return self.filter(active=True, user=None).order_by('name')

class Character(models.Model):
	"""Records information about a players character"""
	
	name = models.CharField("Character name", blank=True, max_length=20, unique=True)
	char_class = models.ForeignKey(RecruitmentClass, verbose_name="Class", blank=True, null=True)
	main_role = models.ForeignKey(CharacterRole, blank=True, null=True)
	rank = models.CharField(max_length=1, choices=RANK_CHOICES, blank=True, null=True)
	user = models.ForeignKey(User, null=True, blank=True)
	ep = models.IntegerField(blank=True, null=True)
	gp = models.IntegerField(blank=True, null=True)
	active = models.BooleanField(default=True)
	
	objects = CharacterManager()
	
	def get_pr(self):
		try:
			base_gp = Settings.objects.get(pk=1).base_gp
		except ObjectDoesNotExist:
			base_gp = 1
		if not base_gp or base_gp == 0:
			base_gp = 1
		return ep / (gp + base_gp)
	
	def __unicode__(self):
		return self.name

ENCOUNTER_REASON_CHOICES = (
	('L', 'Loot'),
	('A', 'Achievement'),
)

class CharacterBossManager(models.Manager):
	use_for_related_fields = True
	
	def get_active(self):
		return self.filter(boss__instance__current=True, boss__is_encounter=True).order_by('boss__instance__ordering', 'boss__ordering', 'boss_detail__ordering', 'boss_detail__name', 'char__name')
	
	def get_by_instance(self, instance):
		return self.filter(boss__instance=instance, boss__is_encounter=True).order_by('boss__instance__ordering', 'boss__ordering', 'boss_detail__ordering', 'boss_detail__name', 'char__name')

class CharacterBoss(models.Model):
	"""Defines which bosses a given character needs"""
	
	char = models.ForeignKey(Character)
	boss = models.ForeignKey(Boss)
	boss_detail = models.ForeignKey(BossDetail, null=True, blank=True)
	reason = models.CharField(null=True, blank=True, max_length=1, choices=ENCOUNTER_REASON_CHOICES)
	notes = models.CharField(null=True, blank=True, max_length=100)
	
	objects = CharacterBossManager()
	
	class Meta:
		unique_together = ('char', 'boss', 'boss_detail')
		verbose_name_plural = "Character bosses"
	
	def __unicode__(self):
		if self.boss_detail:
			detail = ' (' + self.boss_detail.name + ')'
		else:
			detail = '';
		return self.char.name + ' - ' + self.boss.__unicode__() + detail

class Raid(models.Model):
	"""Keeps records of a particular tool session's raid"""
	
	user = models.ForeignKey(User)
	raid_date = models.DateTimeField(blank=True, null=True)
	last_instance = models.ForeignKey(Instance, blank=True, null=True)
	last_boss = models.ForeignKey(Boss, blank=True, null=True)
	last_boss_detail = models.ForeignKey(BossDetail, blank=True, null=True)
	
	class Admin:
		list_display = ('',)
		search_fields = ('',)

	def __unicode__(self):
		return self.user.username + ' (' + self.raid_date.date().isoformat() + ')'

class RaidChar(models.Model):
	"""Keeps record of a given char in a given session's raid"""
	
	raid = models.ForeignKey(Raid)
	char = models.ForeignKey(Character)
	slot = models.IntegerField(blank=True, null=True)

	class Admin:
		list_display = ('',)
		search_fields = ('',)

	def __unicode__(self):
		return self.raid + ' - ' + self.char.name
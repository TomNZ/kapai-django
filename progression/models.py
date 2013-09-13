from django.db import models

class InstanceManager(models.Manager):
	def get_active(self):
		return self.filter(active=True).order_by('ordering')
		
	def get_current(self):
		return self.filter(active=True, current=True).order_by('ordering')
	
	def get_non_current(self):
		return self.filter(active=True, current=False).order_by('ordering')

class Instance(models.Model):
	"""Dungeon instance"""
	
	name = models.CharField(max_length=50)
	cleared_date = models.DateField(blank=True, null=True)
	image_url = models.CharField(blank=True, max_length=200)
	ordering = models.IntegerField(blank=False, default=100)
	players = models.IntegerField(blank=False, default=25)
	current = models.BooleanField(default=True, help_text='Determines whether the instance appears in the progression sidebar, and in the raid tool')
	active = models.BooleanField(default=True, help_text='Determines whether the instance appears on the progression page')
	
	objects = InstanceManager()

	def __unicode__(self):
		return self.name


class BossManager(models.Manager):
	use_for_related_fields = True
	
	def get_active(self):
		return self.filter(active=True).order_by('ordering')
	
	def get_by_instance(self, instance):
		return self.filter(instance=instance, active=True).order_by('ordering')
	
	def get_encounters(self):
		return self.filter(active=True, is_encounter=True).order_by('ordering')

class Boss(models.Model):
	"""Instance boss"""
	
	instance = models.ForeignKey(Instance)
	name = models.CharField(max_length=50)
	cleared_date = models.DateField(blank=True, null=True)
	ordering = models.IntegerField(blank=False, default=100)
	current = models.BooleanField(default=True, help_text='Determines whether the boss appears in the progression sidebar, and in the raid tool')
	is_encounter = models.BooleanField(default=True, help_text='Determines whether the boss is an actual encounter. If false, will not show in raid tool. Useful for showing e.g. drake completion date on the homepage.')
	active = models.BooleanField(default=True)
	
	objects = BossManager()
	
	class Meta:
		verbose_name_plural = "Bosses"

	def __unicode__(self):
		return self.name + ' (' + self.instance.name + ')'


class BossDetailManager(models.Manager):
	use_for_related_fields = True
	
	def get_active(self):
		return self.filter(active=True).order_by('ordering')

	def get_important(self):
		return self.filter(active=True, important=True).order_by('ordering')
	
	def get_by_boss(self, boss):
		return self.filter(boss=boss, active=True).order_by('ordering')

class BossDetail(models.Model):
	"""Detailed boss progression"""
	
	boss = models.ForeignKey(Boss)
	name = models.CharField(max_length=50)
	cleared_date = models.DateField(blank=True, null=True)
	ordering = models.IntegerField(blank=False, default=100)
	important = models.BooleanField(default=True, help_text='Determines whether or not the boss detail appears anywhere on the website. If unticked, will still appear in the raid tool. Useful for achievements.')
	active = models.BooleanField(default=True)
	
	objects = BossDetailManager()

	def __unicode__(self):
		return self.name + ' (' + self.boss.__unicode__() + ')'

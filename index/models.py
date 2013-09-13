from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from datetime import datetime

class SiteProfile(models.Model):
	"""Additional profile fields"""
	
	user = models.ForeignKey(User, unique=True)
	raid_leader = models.BooleanField(default=False)
	raid_admin = models.BooleanField(default=False)

	class Admin:
		list_display = ('',)
		search_fields = ('',)

	def __unicode__(self):
		return u"SiteProfile"

def create_site_profile(sender, instance, created, **kwargs):
	if created:
		profile, created = SiteProfile.objects.get_or_create(user=instance)
post_save.connect(create_site_profile, sender=User)


class Settings(models.Model):
	"""Defines some basic settings for the site"""
	
	base_gp = models.IntegerField(blank=True, null=True)

	def save(self):
		self.id=1
		super(Settings, self).save()
	
	def delete(self):
		pass
		
	class Admin:
		list_display = ('',)
		search_fields = ('',)

	def __unicode__(self):
		return u"Settings"

class NewsItem(models.Model):
	"""News snippet appearing on the home page"""
	
	title = models.CharField(max_length=100)
	when_published = models.DateTimeField(default=datetime.now)
	active = models.BooleanField(default=True)
	body = models.TextField()

	class Admin:
		list_display = ('',)
		search_fields = ('',)

	def __unicode__(self):
		return self.title

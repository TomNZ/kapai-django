from django.db import models

class RecruitmentClassManager(models.Manager):
	def get_active(self):
		return self.filter(active=True).order_by('name')
		
class RecruitmentClass(models.Model):
	"""(RecruitmentClass description)"""
	
	name = models.CharField(max_length=50)
	image_url = models.CharField(blank=True, max_length=200)
	requirements = models.CharField(blank=True, max_length=20, default='None')
	active = models.BooleanField(default=True)
	color = models.CharField(default='FFFFFF', max_length=6)
	
	objects = RecruitmentClassManager()

	class Meta:
		verbose_name_plural = "RecruitmentClasses"
		
	def __unicode__(self):
		return self.name

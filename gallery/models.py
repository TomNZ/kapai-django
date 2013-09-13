from django.db import models

class GalleryManager(models.Manager):
	def get_active(self):
		return self.filter(active=True).order_by('ordering')
		
class Gallery(models.Model):
	"""Gallery instance"""
	
	name = models.CharField(max_length=50)
	created_date = models.DateField(blank=True, null=True)
	ordering = models.IntegerField(blank=False, default=100)
	active = models.BooleanField(default=True)
	slug = models.CharField(blank=False, max_length=20)
	objects = GalleryManager()
	
	class Meta:
		verbose_name_plural = "Galleries"
		
	def __unicode__(self):
		return self.name

class GalleryItemManager(models.Manager):
	use_for_related_fields = True
	
	def get_active(self):
		return self.filter(active=True).order_by('ordering', '-uploaded_date', '-id')
		
class GalleryItem(models.Model):
	"""GalleryItem instance"""
	
	gallery = models.ForeignKey(Gallery)
	
	name = models.CharField(max_length=50)
	uploaded_date = models.DateField(blank=True, null=True)
	large_url = models.CharField(blank=True, max_length=200)
	image_url = models.CharField(blank=True, max_length=200)
	thumb_url = models.CharField(blank=True, max_length=200)
	description = models.TextField(blank=True, max_length=500)
	ordering = models.IntegerField(blank=False, default=100)
	active = models.BooleanField(default=True)
	
	objects = GalleryItemManager()
	
	def __unicode__(self):
		return self.name

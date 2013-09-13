from kapai_django.gallery.models import Gallery, GalleryItem
from django.contrib import admin

class GalleryItemInline(admin.TabularInline):
	model = GalleryItem
	extra = 15

class GalleryAdmin(admin.ModelAdmin):
	inlines = [GalleryItemInline]
	pass

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryItem)
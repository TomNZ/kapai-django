from kapai_django.progression.models import Instance, Boss, BossDetail
from django.contrib import admin

class BossInline(admin.TabularInline):
	model = Boss
	extra = 15

class InstanceAdmin(admin.ModelAdmin):
	inlines = [BossInline]
	pass

class BossDetailInline(admin.TabularInline):
	model = BossDetail
	extra = 5

class BossAdmin(admin.ModelAdmin):
	inlines = [BossDetailInline]
	pass

admin.site.register(Instance, InstanceAdmin)
admin.site.register(Boss, BossAdmin)
admin.site.register(BossDetail)
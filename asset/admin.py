from django.contrib import admin

from .models import Asset, Tag, AssetType, Repair

class AssetAdmin(admin.ModelAdmin):
	list_display = ['model', 'patrimony', 'manufacturer', 'equipment', 'created', 'modified']
	search_fields = ['model', 'patrimony', 'manufacturer__name', 'equipment__name', 'created', 'modified']
	filter_horizontal = ['repair']

class TagAdmin(admin.ModelAdmin):
	list_display = ['name', 'tag', 'asset', 'created', 'modified']
	search_fields = ['name', 'tag', 'asset__model', 'created', 'modified']

class AssetTypeAdmin(admin.ModelAdmin):
	list_display = ['code', 'name', 'created', 'modified']
	search_fields = ['code', 'name', 'created', 'modified']

class RepairAdmin(admin.ModelAdmin):
	list_display = ['name', 'manufacturer', 'created', 'modified']
	search_fields = ['name', 'manufacturer__name', 'created', 'modified']

admin.site.register(Asset, AssetAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(AssetType, AssetTypeAdmin)
admin.site.register(Repair, RepairAdmin)
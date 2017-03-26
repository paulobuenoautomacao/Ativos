from django.contrib import admin

from .models import Asset, AssetTag, AssetType, Criticalness, ControlMesh, ControlMeshTag

class AssetTagAdmin(admin.ModelAdmin):
	list_display = ['name', 'tag', 'asset', 'created', 'modified']
	search_fields = ['name', 'tag', 'asset__model', 'created', 'modified']

class AssetTagInline(admin.StackedInline):
    model = AssetTag
    extra = 1

class AssetAdmin(admin.ModelAdmin):
	list_display = ['model', 'equipment', 'description']
	search_fields = ['model', 'patrimony', 'manufacturer__name', 'equipment__name', 'created', 'modified']
	inlines = [AssetTagInline]

class AssetTypeAdmin(admin.ModelAdmin):
	list_display = ['code', 'name', 'created', 'modified']
	search_fields = ['code', 'name', 'created', 'modified']

class CriticalnessAdmin(admin.ModelAdmin):
	list_display = ['code', 'name', 'created', 'modified']
	search_fields = ['code', 'name', 'created', 'modified']

class ControlMeshTagAdmin(admin.ModelAdmin):
	list_display = ['name', 'tag', 'controlmesh', 'created', 'modified']
	search_fields = ['name', 'tag', 'controlmesh__name', 'created', 'modified']

class ControlMeshTagInline(admin.StackedInline):
    model = ControlMeshTag
    extra = 1

class ControlMeshAdmin(admin.ModelAdmin):
	list_display = ['name', 'assetType', 'equipment', 'created', 'modified']
	search_fields = ['name', 'assetType__name', 'equipment__name' 'created', 'modified']
	filter_horizontal = ['asset']
	inlines = [ControlMeshTagInline]

admin.site.register(Asset, AssetAdmin)
admin.site.register(AssetTag, AssetTagAdmin)
admin.site.register(AssetType, AssetTypeAdmin)
admin.site.register(Criticalness, CriticalnessAdmin)
admin.site.register(ControlMesh, ControlMeshAdmin) 
admin.site.register(ControlMeshTag, ControlMeshTagAdmin)

from django.contrib import admin

from .models import Company, Subsidiary, Department, Local, Equipment, Employee, Manufacturer

class CompanyAdmin(admin.ModelAdmin):
	list_display = ['name', 'created', 'modified']
	search_fields = ['name', 'created', 'modified']

class SubsidiaryAdmin(admin.ModelAdmin):
	list_display = ['code', 'name', 'company', 'created', 'modified']
	search_fields = ['code', 'name', 'company__name', 'created', 'modified']

class DepartmentAdmin(admin.ModelAdmin):
	list_display = ['code', 'name', 'subsidiary', 'created', 'modified']
	search_fields = ['code', 'name', 'subsidiary__name', 'created', 'modified']

class LocalAdmin(admin.ModelAdmin):
	list_display = ['code', 'name', 'department', 'created', 'modified']
	search_fields = ['code', 'name', 'department__name', 'created', 'modified']

class EquipmentAdmin(admin.ModelAdmin):
	list_display = ['code', 'name', 'local', 'created', 'modified']
	search_fields = ['code', 'name', 'local__name', 'created', 'modified']

class EmployeeAdmin(admin.ModelAdmin):
	list_display = ['code', 'name', 'department', 'created', 'modified']
	search_fields = ['code', 'name', 'department__name', 'created', 'modified']

class ManufacturerAdmin(admin.ModelAdmin):
	list_display = ['name', 'company', 'created', 'modified']
	search_fields = ['name', 'company__name', 'created', 'modified']

admin.site.register(Company, CompanyAdmin)
admin.site.register(Subsidiary, SubsidiaryAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Local, LocalAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
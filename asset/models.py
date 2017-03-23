from django.db import models
from core.models import Equipment, Manufacturer

class Asset(models.Model):

	model = models.CharField('Modelo', max_length=100)
	assetType = models.ForeignKey('AssetType', on_delete=models.PROTECT, verbose_name='Tipo de ativo')
	patrimony = models.CharField('Patrimônio', max_length=20, blank=True)
	description	= models.TextField('Descrição', blank=True)
	manufacturer = models.ForeignKey('core.Manufacturer', on_delete=models.PROTECT, verbose_name='Fabricante')
	equipment = models.ForeignKey('core.Equipment', verbose_name='Equipamento')
	repair = models.ManyToManyField('Repair', verbose_name='Reparos', blank=True)
	created	= models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	def __str__(self):
		return self.model

	class Meta:
		verbose_name = 'Equipamento'
		verbose_name_plural = 'Equipamentos'
		ordering = ['equipment']

class Tag(models.Model):

	name = models.CharField('Nome', max_length=100)
	tag = models.CharField('TAG', max_length=50)
	asset = models.ForeignKey('Asset', on_delete=models.CASCADE, verbose_name='Equipamento')
	created	= models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	def __str__(self):
		return '%s %s' % (self.name, self.tag)

	class Meta:
		verbose_name = 'TAG'
		verbose_name_plural = 'TAGs'
		ordering = ['tag']

class AssetType(models.Model):

	code = models.CharField('Código', max_length=4)
	name = models.CharField('Nome', max_length=100)
	description	= models.TextField('Descrição', blank=True)
	created	= models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	def __str__(self):
		return '%s %s' % (self.code, self.name)

	class Meta:
		verbose_name = 'Tipo de Ativo'
		verbose_name_plural = 'Tipos de Ativos'
		ordering = ['name']

class Repair(models.Model):

	name = models.CharField('Nome', max_length=100)
	description	= models.TextField('Descrição', blank=True)
	manufacturer = models.ForeignKey('core.Manufacturer', on_delete=models.PROTECT, verbose_name='Fabricante')
	created	= models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Reparo'
		verbose_name_plural = 'Reparos'
		ordering = ['name']
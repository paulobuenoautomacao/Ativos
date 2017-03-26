from django.db import models
from core.models import Equipment, Manufacturer

class Asset(models.Model):

	model = models.CharField('Modelo', max_length=100)
	assetType = models.ForeignKey('AssetType', on_delete=models.PROTECT, verbose_name='Tipo de ativo')
	patrimony = models.CharField('Patrimônio', max_length=20, blank=True)
	description	= models.TextField('Descrição', blank=True)
	manufacturer = models.ForeignKey('core.Manufacturer', on_delete=models.PROTECT, verbose_name='Fabricante', null=True, blank=True)
	equipment = models.ForeignKey('core.Equipment', on_delete=models.PROTECT, verbose_name='Equipamento')
	criticalness = models.ForeignKey('Criticalness', on_delete=models.PROTECT, verbose_name='Criticidade', null=True, blank=True)
	created	= models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	def __str__(self):
		return self.model

	class Meta:
		verbose_name = 'Ativo'
		verbose_name_plural = 'Ativos'
		ordering = ['equipment', 'assetType']

class AssetTag(models.Model):

	name = models.CharField('Nome', max_length=100)
	tag = models.CharField('TAG', max_length=50)
	asset = models.ForeignKey('Asset', on_delete=models.CASCADE, verbose_name='Ativo')
	created	= models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	def __str__(self):
		return '%s %s' % (self.name, self.tag)

	class Meta:
		verbose_name = 'TAG do Ativo'
		verbose_name_plural = 'TAGs dos Ativos'
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

class Criticalness(models.Model):

	code = models.CharField('Código', max_length=4)
	name = models.CharField('Nome', max_length=100)
	description	= models.TextField('Descrição', blank=True)
	created	= models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Criticidade'
		verbose_name_plural = 'Criticidades'
		ordering = ['code']

class ControlMesh(models.Model):

	name = models.CharField('Nome', max_length=100)
	description	= models.TextField('Descrição', blank=True)
	assetType = models.ForeignKey('AssetType', on_delete=models.PROTECT, verbose_name='Tipo de malha')
	equipment = models.ForeignKey('core.Equipment', on_delete=models.PROTECT, verbose_name='Equipamento')
	criticalness = models.ForeignKey('Criticalness', on_delete=models.PROTECT, verbose_name='Criticidade', blank=True)
	asset = models.ManyToManyField('Asset', verbose_name='Ativos', blank=True)
	created	= models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Malha de controle'
		verbose_name_plural = 'Malhas de controle'
		ordering = ['equipment']

class ControlMeshTag(models.Model):

	name = models.CharField('Nome', max_length=100)
	tag = models.CharField('TAG', max_length=50)
	controlmesh = models.ForeignKey('ControlMesh', on_delete=models.CASCADE, verbose_name='Malha de controle')
	created	= models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	def __str__(self):
		return '%s %s' % (self.name, self.tag)

	class Meta:
		verbose_name = 'TAG da Malha de controle'
		verbose_name_plural = 'TAGs das Malhas de controle'
		ordering = ['tag']
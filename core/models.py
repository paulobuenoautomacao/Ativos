from django.db import models

class Company(models.Model):

	name = models.CharField('Nome', max_length=100)
	description	= models.TextField('Descrição', blank=True)
	created	= models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Compania'
		verbose_name_plural = 'Companias'
		ordering = ['name']


class Subsidiary(models.Model):

	code = models.CharField('Código', max_length=4)
	name = models.CharField('Nome', max_length=100)
	description	= models.TextField('Descrição', blank=True)
	company = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name='Compania')
	created	= models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	def __str__(self):
		return '%s %s' % (self.code, self.name)

	class Meta:
		verbose_name = 'Unidade'
		verbose_name_plural = 'Unidades'
		ordering = ['code']

class Department(models.Model):

	code = models.CharField('Código', max_length=2)
	name = models.CharField('Nome', max_length=100)
	description	= models.TextField('Descrição', blank=True)
	subsidiary = models.ForeignKey('Subsidiary', on_delete=models.CASCADE, verbose_name='Unidade')
	created	= models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	def __str__(self):
		return '%s %s' % (self.code, self.name)

	class Meta:
		verbose_name = 'Departamento'
		verbose_name_plural = 'Departamentos'
		ordering = ['code']

class Local(models.Model):

	code = models.CharField('Código', max_length=5)
	name = models.CharField('Nome', max_length=100)
	description	= models.TextField('Descrição', blank=True)
	department = models.ForeignKey('Department', on_delete=models.CASCADE, verbose_name='Departamento')
	created	= models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	def __str__(self):
		return '%s %s' % (self.code, self.name)

	class Meta:
		verbose_name = 'Local'
		verbose_name_plural = 'Locais'
		ordering = ['code']

class Equipment(models.Model):

	code = models.CharField('Código', max_length=10)
	name = models.CharField('Nome', max_length=100)
	description	= models.TextField('Descrição', blank=True)
	local = models.ForeignKey('Local',  on_delete=models.CASCADE, verbose_name='Local')
	created	= models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	def __str__(self):
		return '%s %s' % (self.code, self.name)

	class Meta:
		verbose_name = 'Equipamento'
		verbose_name_plural = 'Equipamentos'
		ordering = ['code']

class Employee(models.Model):

	code = models.CharField('Código', max_length=10)
	name = models.CharField('Nome', max_length=100)
	position = models.TextField('Cargo', blank=True)
	department = models.ForeignKey('Department', on_delete=models.CASCADE, verbose_name='Departamento')
	created	= models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	def __str__(self):
		return '%s %s' % (self.code, self.name)

	class Meta:
		verbose_name = 'Funcionário'
		verbose_name_plural = 'Funcionários'
		ordering = ['name']

class Manufacturer(models.Model):

	name = models.CharField('Nome', max_length=100)
	description	= models.TextField('Descrição', blank=True)
	company = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name='Compania')
	created	= models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	def __str__(self):
		return self.name
		
	class Meta:
		verbose_name = 'Fabricante'
		verbose_name_plural = 'Fabricantes'
		ordering = ['name']
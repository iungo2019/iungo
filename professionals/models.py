from django.db import models
from django.utils.text import slugify



# Create your models here.
class Professionals(models.Model):
	name = models.CharField(max_length=50)
	category = models.ForeignKey('Category', null=True ,on_delete=models.SET_NULL)
	projects_completed = models.PositiveIntegerField()
	happy_customers = models.PositiveIntegerField()
	max_budget = models.PositiveIntegerField()
	min_budget = models.PositiveIntegerField()
	profile_image = models.ImageField(upload_to='profile/' ,null=True)
	banner_image = models.ImageField(upload_to='banner/' ,null=True)
	pincode = models.PositiveIntegerField(null=True)
	city = models.CharField(max_length=50, null=True)
	description = models.TextField()
	short_description = models.TextField(null=True)
	email = models.EmailField(null=True)
	phone_number = models.CharField(max_length=15 ,null=True)
	phone_number_1 = models.CharField(max_length=15 ,null=True)
	website = models.URLField(max_length=200, null=True)
	company_name = models.CharField(max_length=50 ,null=True)
	address = models.TextField(null=True)
	facebook_link = models.URLField(max_length=200, null=True)
	instagram_link = models.URLField(max_length=200, null=True)
	youtube_link = models.URLField(max_length=200, null=True)
	experience = models.PositiveIntegerField(null=True)


	slug = models.SlugField(blank=True, null=True)



	def save(self, *args, **kargs):
		if not self.slug and self.name :
			self.slug = slugify(self.name)
		super(Professionals , self).save(*args, **kargs)



	def __str__(self):
		return self.name


	class Meta:
		verbose_name = 'Professional'
		verbose_name_plural = 'Professionals'




class Category(models.Model):
	category_name = models.CharField(max_length=50)
	image = models.ImageField(upload_to='categoryprofessionals/' ,null=True)



	def __str__(self):
		return self.category_name



	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'






class ProfessionalOffice(models.Model):
	professional = models.ForeignKey(Professionals , on_delete=models.CASCADE)
	image = models.ImageField(upload_to='ProfessionalOffice/' , blank=True , null=True)


	def __str__(self):
		return self.professional.name



	class Meta:
		verbose_name = 'ProfessionalOffice'
		verbose_name_plural = 'ProfessionalOffices'





class ProjectImages(models.Model):
	professional = models.ForeignKey(Professionals , on_delete=models.CASCADE)
	image = models.ImageField(upload_to='proprojectimages/' , blank=True , null=True)


	def __str__(self):
		return self.professional.name

	class Meta:
		verbose_name = 'Project Image'
		verbose_name_plural = 'Project Images'



class Reserve(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	phone_number = models.CharField(max_length=15 ,null=True)

	def __str__(self):
		return self.name

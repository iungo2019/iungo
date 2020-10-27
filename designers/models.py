from django.db import models
from django.utils.text import slugify



banks_approved = (
	('Axis Bank' , 'Axis Bank'),
	('Bandhan Bank' , 'Bandhan Bank'),
	('CSB Bank' , 'CSB Bank'),
	('City Union Bank' , 'City Union Bank'),
	('DCB Bank' , 'DCB Bank'),
	('Dhanlaxmi Bank' , 'Dhanlaxmi Bank'),
	('Federal Bank' , 'Federal Bank'),
	('HDFC Bank' , 'HDFC Bank'),
	('ICICI Bank' , 'ICICI Bank'),
	('IDBI Bank' , 'IDBI Bank'),
	('IDFC First Bank' , 'IDFC First Bank'),
	('IndusInd Bank' , 'IndusInd Bank'),
	('Karnataka Bank' , 'Ready to move'),
	('Karur Vysya Bank' , 'Karur Vysya Bank'),
	('Kotak Mahindra Bank' , 'Kotak Mahindra Bank'),
	('Lakshmi Vilas Bank' , 'Lakshmi Vilas Bank'),
	('Nainital Bank' , 'Nainital Bank'),
	('RBL Bank' , 'RBL Bank'),
	('South Indian Bank' , 'South Indian Bank'),
	('Tamilnad Mercantile Bank Limited' , 'Tamilnad Mercantile Bank Limited'),
	('Yes Bank' , 'Yes Bank'),


)

Project_Consultation  = (
	('Available' , "availbale"),
	('Not available ' , "Not available"),
)


Project_Design = (
	('Available' , "availbale"),
	('Not available ' , "Not available"),
)


Production = (
	('Available' , "availbale"),
	('Not available ' , "Not available"),
)

Furniture_design = (
	('Available' , "availbale"),
	('Not available ' , "Not available"),
)

Design_Consultancy = (
	('Available' , "availbale"),
	('Not available ' , "Not available"),
)


Home_Advising = (
	('Available' , "availbale"),
	('Not available ' , "Not available"),
)


Remodeling = (
	('Available' , "availbale"),
	('Not available ' , "Not available"),
)



# Create your models here.
class Designers(models.Model):
	name = models.CharField(max_length=50)
	category = models.ForeignKey('Category', null=True ,on_delete=models.SET_NULL)
	style = models.ForeignKey('Style', null=True ,on_delete=models.SET_NULL)
	projects_completed = models.PositiveIntegerField()
	projects_ongoing = models.PositiveIntegerField()
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
	alternate_phone_number = models.CharField(max_length=15 , null=True)
	website = models.URLField(max_length=200, null=True)
	company_name = models.CharField(max_length=50 ,null=True)
	address = models.TextField(null=True)
	facebook_link = models.URLField(max_length=200, null=True)
	instagram_link = models.URLField(max_length=200, null=True)
	youtube_link = models.URLField(max_length=200, null=True)
	experience = models.PositiveIntegerField(null=True)
	Project_Consultation = models.CharField(choices=Project_Consultation , max_length = 50, null=True)
	Project_Design = models.CharField(choices=Project_Design , max_length = 50, null=True)
	Production = models.CharField(choices=Production , max_length = 50, null=True)
	Furniture_design = models.CharField(choices=Furniture_design , max_length = 50, null=True)
	Design_Consultancy = models.CharField(choices=Design_Consultancy , max_length = 50, null=True)
	Home_Advising = models.CharField(choices=Home_Advising , max_length = 50, null=True)
	Remodeling = models.CharField(choices=Remodeling , max_length = 50, null=True)


	slug = models.SlugField(blank=True, null=True)


	def save(self, *args, **kargs):
		if not self.slug and self.name :
			self.slug = slugify(self.name)
		super(Designers , self).save(*args, **kargs)



	def __str__(self):
		return self.name


	class Meta:
		verbose_name = 'Designer'
		verbose_name_plural = 'Designers'




class Category(models.Model):
	category_name = models.CharField(max_length=50)
	image = models.ImageField(upload_to='category/' ,null=True)



	def __str__(self):
		return self.category_name



	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'






class Style(models.Model):
	style_name = models.CharField(max_length=50)
	image = models.ImageField(upload_to='Style/' ,null=True)



	def __str__(self):
		return self.style_name



	class Meta:
		verbose_name = 'Style'
		verbose_name_plural = 'Styles'



class DesignerOffice(models.Model):
	designer = models.ForeignKey(Designers , on_delete=models.CASCADE)
	image = models.ImageField(upload_to='DesignerOffice/' , blank=True , null=True)


	def __str__(self):
		return self.designer.name



	class Meta:
		verbose_name = 'DesignerOffice'
		verbose_name_plural = 'DesignerOffices'





class Banks_approved(models.Model):
	designer = models.ForeignKey(Designers , on_delete=models.CASCADE)
	banks_approved = models.CharField(choices=banks_approved ,max_length = 50, null=True)
	loan_details = models.TextField()

	def __str__(self):
		return self.designer.name


	class Meta:
		verbose_name = 'Bank approved'
		verbose_name_plural = 'Banks approved'



class ProjectImages(models.Model):
	designer = models.ForeignKey(Designers , on_delete=models.CASCADE)
	image = models.ImageField(upload_to='projectimages/' , blank=True , null=True)


	def __str__(self):
		return self.designer.name

	class Meta:
		verbose_name = 'Project Image'
		verbose_name_plural = 'Project Images'



class Reserve(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	phone_number = models.CharField(max_length=15 ,null=True)
	pincode = models.CharField(max_length=15 ,null=True)
	Requirements = models.TextField()

	def __str__(self):
		return self.name

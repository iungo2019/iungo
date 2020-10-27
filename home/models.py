from django.db import models



Testinomial_client_type  = (
	('Interior designer' , "Interior designer"),
	('Architect ' , "Architect"),
	('Builder' , "Builder" ),
	('Customer' , "Customer"),
)

social_media  = (
	('Facebook' , "Facebook"),
	('Instagram' , "Instagram"),
	('Twitter' , "Twitter" ),
	('Google' , "Google"),
)

# Create your models here.
class Home(models.Model):
	name = models.CharField(max_length=50)
	banner_image1 = models.ImageField(upload_to='home_banner/' ,null=True)
	banner_image2 = models.ImageField(upload_to='home_banner/' ,null=True)
	banner_image3 = models.ImageField(upload_to='home_banner/' ,null=True)
	banner_content1 = models.CharField(max_length=200)
	banner_content2 = models.CharField(max_length=200)
	banner_content3 = models.CharField(max_length=200)
	banner_description1 = models.TextField()
	banner_description2 = models.TextField()
	banner_description3 = models.TextField()



	def __str__(self):
		return self.name






class Testinomials(models.Model):
	name = models.CharField(max_length=50)
	profile_pic = models.ImageField(upload_to='home_profile/' ,null=True)
	revied_by = models.CharField(choices=Testinomial_client_type , max_length = 50, null=True)
	via = models.CharField(choices=social_media , max_length = 50, null=True)
	content = models.TextField()


	def __str__(self):
		return self.name
